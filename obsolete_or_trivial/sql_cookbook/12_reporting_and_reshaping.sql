-- 12.1 pivot a result set into one row
-- postgres has the crosstab() function

-- book solution ugly and hardcodes number of columns
select sum(case when deptno = 10 then 1 else 0 end) as deptno_10,
sum(case when deptno = 20 then 1 else 0 end) as deptno_20,
sum(case when deptno = 30 then 1 else 0 end) as deptno_30
from emp;


-- 12.2 pivot a result set into multiple rows
-- use row_number() over (partition by job order by ename)

-- 12.3 reverse a pivot

-- 12.4 reverse pivot a result set

-- 12.5 suppress repeating values
-- use LAG

select case when lag(deptno) over (order by deptno) = deptno then null else deptno end deptno,
ename from emp;

-- 12.6 pivot a result set to facilitate inter-row calculations

-- 12.7 create buckets of fixed size

select ceil(row_number() over (order by empno) / 5.0) grp,
empno, ename from emp;

-- 12.8 create a specific number of buckets

select ntile(4) over (order by empno) grp,
empno, ename
from emp;

-- 12.9 create horizontal histograms

select deptno, rpad('', count(*)::integer, '*') cnt
from emp
group by deptno;

-- 12.10 vertical histogram
-- too specific

-- 12.11 returning non-group by columns
-- use max/min() over ()

-- 12.12 calculating simple subtotals

select coalesce(job, 'total') job,
sum(sal) sal
from emp
group by rollup(job)
order by sal;

-- 12.13 subtotals for all possible combinations
--SKIP-- too obscure, uses CUBE()

-- 12.14 identify rows that are not subtotals

select deptno, job, sum(sal) sal,
grouping(deptno) deptno_subtotals,
grouping(job) job_subtotals
from emp
group by cube(deptno, job)
order by deptno, sal;


-- 12.15 use case to flag rows

select ename,
  case when job = 'CLERK' then 1 else 0 end as is_clerk,
  case when job = 'MANAGER' then 1 else 0 end as is_mgr,
  case when job = 'PRESIDENT' then 1 else 0 end as is_prez
from emp;


-- 12.16 sparse matrix

select case deptno when 10 then ename end as d10,
case job when 'CLERK' then ename end as clerks
from emp;


-- 12.17 group rows by units of time

-- assume one id is one second
select ceil(trx_id/5.0) as grp,
min(trx_date) as trx_start,
max(trx_date) as trx_end,
sum(trx_cnt) as total
from trx_log
group by ceil(trx_id/5.0);


-- 12.18 aggregate over different groups/partitions simultaneously

select ename, job, deptno,
count(*) over (partition by deptno) dept_ct,
count(*) over (partition by job) job_ct,
count(*) over () total
from emp;


-- 12.19 aggregations over a moving range of values

select e.hiredate,
e.sal,
(select sum(sal) from emp d
  where d.hiredate between e.hiredate - 90 and e.hiredate) as spending_pattern
from emp e
order by e.hiredate;


-- 12.20 pivot a result set with subtotals
--SKIP-- too specific
