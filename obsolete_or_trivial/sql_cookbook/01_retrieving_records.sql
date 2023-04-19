-- 1.2
select *
from emp
where deptno = 10;


-- 1.3
select *
from emp
where deptno = 10
or comm is not null
or sal <= 2000 and deptno = 20


-- 1.5
select sal as salary, comm as commission
from emp;


-- 1.6
-- to use aliased names, use a subquery (inline view)
select *
from (
  select sal as salary, comm as commission
  from emp
) x -- subquery must have an alias
where salary < 3000;


-- 1.7 concatenating values
select ename || ' works as a ' || job as msg
from emp
where deptno = 10;


-- 1.8 conditional logic in select

select ename, sal,
  case when sal <= 2000 then 'underpaid'
       when sal >= 4000 then 'overpaid'
       else 'ok'
  end as status
from emp;


-- 1.9 limit number of rows returned

select *
from emp limit 5;


-- 1.10 random subset

select ename, job
from emp
order by random() limit 5;


-- 1.11 null values

select *
from emp
where comm is null;


-- 1.12 replace null with a real value

select ename, coalesce(comm, 0)
from emp;


-- 1.13a search inside a set
select ename
from emp
where deptno in (10, 20);


-- 1.13b search for a pattern

select ename, job
from emp
where ename like '%I%' or job like '%ER';
