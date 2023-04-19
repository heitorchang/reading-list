-- 2.1

select ename, job, sal
from emp
where deptno = 10
order by sal desc; -- highest first (descending)


-- 2.2
-- order by deptno, sal desc;


-- 2.3 sort by substring
select ename, job
from emp
order by substr(job, length(job) - 1);


-- 2.4 sorting mixed alphanumeric data

create view V2_4
as
select ename || ' ' || deptno as data
from emp;

--SKIP-- TRANSLATE/REPLACE is used


-- 2.5 dealing with nulls when sorting

-- use an auxiliary column is_null

select ename, sal, comm,
  case when comm is null then 0 else 1 end as is_null
from emp;


-- 2.6 sorting on a data-dependent key

select ename, sal, job, comm
from emp
order by case when job = 'SALESMAN' then comm else sal end;
