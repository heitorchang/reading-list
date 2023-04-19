-- 11.1 paginating through a result set

select sal from (
  select row_number() over (order by sal) as rn,
  sal
  from emp
) x
where rn between 1 and 5;
-- 'between 6 and 10' for those rows
-- there is no IndexError

-- also:
select ename, sal from emp order by sal limit 3 offset 5;

-- 11.2 skipping n rows from a table

-- skips every other row
select ename
from (
  select row_number() over (order by ename) rn,
  ename
  from emp
) x
where mod(rn, 2) = 1;


-- 11.3 incorporating OR logic in outer joins

select e.ename, d.deptno, d.dname, d.loc
from dept d left join emp e
on d.deptno = e.deptno and e.deptno in (10, 20)
order by d.deptno;


-- 11.4 determine which rows are reciprocals
-- 70, 90 and 90, 70 are reciprocals

-- idea: self-join
select distinct v1.*
from V v1, V v2
where v1.test1 = v2.test2
and v1.test2 = v2.test1
and v1.test1 <= v1.test2;  -- avoid duplicates


-- 11.5 selecting the top n records

select ename, sal from (
  select ename, sal, dense_rank() over (order by sal desc) dr
  from emp
) x
where dr <= 5;

-- this query returns 6 rows because of a repeated salary.
-- limit 5 returns 5 rows regardless of value


-- 11.6 finding records with the highest and lowest values

select ename, sal
from (
select ename, sal,
min(sal) over () min_sal,
max(sal) over () max_sal
from emp
) x
where sal in (min_sal, max_sal);


-- 11.7 investigating future rows

-- find employees who earn less than the one hired immediately after them

select ename, sal, hiredate
from (
select ename, sal, hiredate,
lead(sal) over (order by hiredate) next_sal
from emp
) x
where sal < next_sal;


-- 11.8 shifting row values

select ename, sal,
coalesce(lead(sal) over (order by sal), min(sal) over ()) fwd,
coalesce(lag(sal) over (order by sal), max(sal) over ()) rew
from emp;


-- 11.9 ranking results

select dense_rank() over (order by sal) rnk,
sal
from emp;


-- 11.10 suppressing duplicates

select distinct job from emp;


-- 11.11 finding knight values (like a chess knight that jumps)

select deptno, ename, sal, hiredate, max(latest_sal) over (partition by deptno) latest_sal
from (
select deptno, ename, sal, hiredate, case when hiredate = max(hiredate) over (partition by deptno) then sal else 0 end latest_sal
from emp
) x
order by deptno, hiredate;


-- 11.12 generating simple forecasts

-- return additional rows and columns representing future actions

select id, order_date, process_date,
  case when gs.n = 2
    then process_date + 1
    else null
  end as verified,
  case when gs.n = 3
    then process_date + 2
    else null
  end as shipped
from (
  select gs.id,
    current_date + gs.id as order_date,
    current_date + gs.id + 2 as process_date
  from generate_series(1, 3) gs(id)
) orders,
generate_series(1, 3) gs(n);
