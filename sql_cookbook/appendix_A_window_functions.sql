-- grouping

Grouping is a way to organize similar rows together. Each row in the result set is a group and represents one or more rows with the same values in one or more specified columns.

Examples:
* all employees in dept. 10
* all clerks

select deptno, count(*) as cnt, max(sal) as hi_sal, min(sal) as lo_sal
from emp
where deptno = 10
group by deptno;

-- mathematical definition

a group is (G o e), where G is a set, o is a binary function, and e is a member of G (a row)

since groups are distinct, there is no need to use the DISTINCT keyword. However, they serve different purposes.

Russell's barber paradox (raises a contradiction):'

In a certain town, there is a male barber who shaves all men, and only those men who do not shave themselves. Who shaves the barber?

If he shaves himself, then it is not the case that he shave men who do not shave themselves.

But if he does not shave himself, then he must be obligated to shave himself.


select coalesce(name, 'NULL') as name,
count(name) as cnt
from fruits
group by name;

will return 'NULL': 0.

To count the null rows, use count(*) instead.


constants, scalars, window functions and noncorrelated scalar subqueries do not require a GROUP BY clause.

select 'hello' as msg,
1 as num,
deptno,
(select count(*) from emp) as total,
count(*) as cnt
from emp
group by deptno;


select deptno, job, count(*) as cnt
from emp
group by deptno, job;


-- Windowing

like aggregate functions, window functions perform aggregation on a group of rows, but can return multiple values for each group.

the group of rows to perform the aggregation on is the window.

select ename, deptno, count(*) over () as cnt
from emp
order by deptno;


window functions are performed as the second-to-last step (before order by)

select ename,
deptno,
count(*) over () as cnt
from emp
where deptno = 10
order by deptno;


PARTITION BY defines a group of rows to perform an aggregation over.

it is like a "moving GROUP BY"

select ename, deptno, count(*) over (partition by deptno) as cnt
from emp
order by deptno;


-- more efficient than
select e.ename,
e.deptno,
(select count(*) from emp d
 where e.deptno = d.deptno) as cnt
from emp e
order by e.deptno;


select ename, deptno,
  count(*) over (partition by deptno) as dept_cnt,
  job,
  count(*) over (partition by job) as job_cnt
from emp
order by deptno;


-- Effect of NULLs

similar to the effect on GROUP BYs

select coalesce(comm, -1) as comm,
count(*) over (partition by comm) as cnt
from emp;

returns
-1 | 10

if count(comm) is used,
-1 |  0 will be returned


partitions may have an ORDER BY clause

select deptno, ename, hiredate, sal,
  sum(sal) over (partition by deptno) as total1,
  sum(sal) over () as total2,
  sum(sal) over (order by hiredate) as running_total
from emp
where deptno = 10;

ORDER BY creates a "moving" window behind the scenes.

-- Art of PostgreSQL Ch. 17
over (order by x) is actually over (order by x rows between unbounded preceding and current row)

'rows between' looks at the order of rows
'range between' uses the ORDER BY clause to determine inclusion in a window.


-- RANGE BETWEEN / ROWS BETWEEN (framing clause)

select deptno, ename, hiredate, sal,
  sum(sal) over (partition by deptno) as total1,
  sum(sal) over () as total2,
  sum(sal) over (order by hiredate
                range between unbounded preceding and current row) as running_total
from emp
where deptno = 10;


select deptno, ename, sal,
  sum(sal) over (order by hiredate
                range between unbounded preceding and current row) as run_total1,
  sum(sal) over (order by hiredate
                rows between 1 preceding and current row) as run_total2,
  sum(sal) over (order by hiredate
                range between current row and unbounded following) as run_total3,
  sum(sal) over (order by hiredate
                 rows between current row and 1 following) as run_total4
from emp
where deptno = 10;


select ename, sal,
  min(sal) over (order by sal) min1,
  max(sal) over (order by sal) max1,
  min(sal) over (order by sal
    range between unbounded preceding and unbounded following) min2,
  max(sal) over (order by sal
    range between unbounded preceding and unbounded following) max2,
  min(sal) over (order by sal
    range between current row and current row) min3,
  max(sal) over (order by sal
    range between current row and current row) max3,
  max(sal) over (order by sal
    rows between 3 preceding and 3 following) max4
from emp;


-- how many employees are there in each dept.? how many different types of employees are in each dept.?

select deptno, job,
count(*) over (partition by deptno) as emp_cnt,
count(job) over (partition by deptno, job) as job_cnt,
count(*) over () as total
from emp;

-- equivalent to
select a.deptno, a.job,
  (select count(*) from emp b
   where b.deptno = a.deptno) as emp_cnt,
  (select count(*) from emp b
   where b.deptno = a.deptno and b.job = a.job) as job_cnt,
  (select count(*) from emp) as total
from emp a
order by deptno, job;


select deptno,
  emp_cnt as dept_total,
  total,
  max(case when job = 'CLERK' then job_cnt else 0 end) as clerks,
  max(case when job = 'PRESIDENT' then job_cnt else 0 end) as prez -- WRONG! prez appears as 1 for dept. 10, but his dept. is NULL
  from (
   select deptno,
    job,
    count(*) over (partition by deptno) as emp_cnt,
    count(job) over (partition by deptno, job) as job_cnt,
    count(*) over () as total
   from emp
   ) x
group by deptno, emp_cnt, total;


-- remove duplicates
select distinct deptno, count(*) over (partition by deptno) emp_count from emp;
