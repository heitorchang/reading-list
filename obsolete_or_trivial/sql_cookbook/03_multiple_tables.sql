-- 3.1 stacking rowsets

select ename as ename_and_dname, deptno
from emp
where deptno = 10
union all
select '----------', null
from t1 -- returns one row
union all
select dname, deptno
from dept;

-- UNION most likely sorts to remove duplicates, so it may come with
-- a performance cost


-- 3.2 combining related rows

select e.ename, d.loc
from emp e
join dept d
on e.deptno = d.deptno
where e.deptno = 10;


-- 3.3 finding rows in common between two tables

create view V3_3
as
select ename, job, sal
from emp
where job = 'CLERK';

select empno, ename, job, sal, deptno
from emp
where (ename, job, sal) in (
  select ename, job, sal from emp
  intersect
  select ename, job, sal from V3_3
);


-- 3.4 retrieving values from one table that do not exist in another

select deptno from dept
except
select deptno from emp;

-- correlated subquery: rows from the outer query are referenced in the subquery.

select d.deptno
from dept d
where not exists (
  select 1
  from emp e
  where d.deptno = e.deptno
);


-- 3.5 retrieving rows from one table that do not correspond to rows in another (do not have a match in the other table)

select d.*
from dept d left join emp e
on d.deptno = e.deptno
where e.deptno is null;


-- 3.6 adding joins to a query without interfering with other joins

select e.ename, d.loc, eb.received
from emp e join dept d
on e.deptno = d.deptno
left join emp_bonus eb
on e.empno = eb.empno
order by d.loc, e.ename;

-- OR

select e.ename, d.loc,
  (select eb.received from emp_bonus eb
   where e.empno = eb.empno) as received
from emp e, dept d
where e.deptno = d.deptno
order by d.loc, e.ename;


-- 3.7 determine whether two tables have the same data

-- use EXCEPT and UNION ALL to find the difference between a view V3_7 and table EMP

create view V3_7 as
select * from emp where deptno != 10
union all
select * from emp where ename = 'WARD';

-- find rows in EMP that do not exist in V3_7
-- combine (UNION ALL) with rows from V3_7 that do not exist in EMP

(
 select empno, ename, job, mgr, hiredate, sal, comm, deptno, count(*) as cnt
 from V3_7
 group by empno, ename, job, mgr, hiredate, sal, comm, deptno
 except
 select empno, ename, job, mgr, hiredate, sal, comm, deptno, count(*) as cnt
 from emp
 group by empno, ename, job, mgr, hiredate, sal, comm, deptno
)
union all
(
 select empno, ename, job, mgr, hiredate, sal, comm, deptno, count(*) as cnt
 from emp
 group by empno, ename, job, mgr, hiredate, sal, comm, deptno
 except
 select empno, ename, job, mgr, hiredate, sal, comm, deptno, count(*) as cnt
 from V3_7
 group by empno, ename, job, mgr, hiredate, sal, comm, deptno
)

-- 3.8 avoiding cartesian products

select e.ename, d.loc
from emp e
join dept d on e.deptno = d.deptno
where e.deptno = 10;

-- if you really wanted a cartesian product, don't join
select e.ename, d.loc
from emp e, dept d
where e.deptno = 10;


-- 3.9 joining when using aggregates

-- bonuses are percentages. 1 = 10%, 2 = 20%, 3 = 30%
-- an incorrect value might be returned due to duplicates.
-- solutions:
-- * use DISTINCT
-- * aggregate first in an inline view

select deptno,
  sum(distinct sal) as total_sal, -- WRONG! if MILLER also has 5000,
                                  -- it will be dropped
  sum(bonus) as total_bonus
from (
  select e.empno, e.ename, e.sal, e.deptno,
  e.sal * case when eb.type = 1 then 0.1
               when eb.type = 2 then 0.2
               else 0.3
          end as bonus
  from emp e, emp_bonus_3_9 eb
  where e.empno = eb.empno
  and e.deptno = 10
) x
group by deptno;

-- corrected version
select d.deptno,
  d.total_sal,
  sum(e.sal * case when eb.type = 1 then 0.1
                   when eb.type = 2 then 0.2
                   else 0.3
              end) as total_bonus
from emp e,
emp_bonus_3_9 eb,
(
  select deptno, sum(sal) as total_sal
  from emp
  where deptno = 10
  group by deptno
) d
where e.deptno = d.deptno
and e.empno = eb.empno
group by d.deptno, d.total_sal;

-- window function
select e.empno, e.ename,
  sum(distinct e.sal) over -- same problem, assumes no duplicates
                           -- Postgres 13 does not have distinct
                           -- for window functions
  (partition by e.deptno) as total_sal,
  e.deptno,
  sum(e.sal * case when eb.type = 1 then 0.1
                   when eb.type = 2 then 0.2
                   else 0.3
              end) over
    (partition by deptno) as total_bonus
  from emp e, emp_bonus_3_9 eb
  where e.empno = eb.empno
  and e.deptno = 10;


-- 3.10 outer joins with aggregates

select d.deptno,
  d.total_sal,
  sum(e.sal * case when eb.type = 1 then 0.1
                   when eb.type = 2 then 0.2
                   else 0.3
              end) as total_bonus
  from emp e,
  emp_bonus_3_10 eb,
  (select deptno, sum(sal) as total_sal
   from emp
   where deptno = 10
   group by deptno
  ) d
  where e.deptno = d.deptno
    and e.empno = eb.empno
  group by d.deptno, d.total_sal;


-- 3.11 returning missing data from multiple tables

-- employee without dept used for testing
-- insert into emp (empno, ename,   job,          mgr, hiredate,      sal, comm, deptno) select 1111, 'YODA',  'JEDI',     null, '01-JAN-2001', sal,  comm, null from emp where ename = 'KING';

-- use FULL JOIN
select d.deptno, d.dname, e.ename
from dept d full join emp e
on d.deptno = e.deptno;


-- 3.12 using NULLs in operations and comparisons

-- find employees whose commission is less than WARD's

select ename, comm, coalesce(comm, 0)
from emp
where coalesce(comm, 0) < (select comm
                           from emp
                           where ename = 'WARD');
