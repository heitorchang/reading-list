-- 4.1 inserting

insert into dept (deptno, dname, loc)
values
(50, 'PROGRAMMING', 'BALTIMORE'),
(60, 'HR', 'LOS ANGELES');


-- 4.2 inserting default values

create table D (
  id integer default 0
);

insert into D values (default);


-- 4.3 overriding a default value with null

-- specify null in the values list

insert into d (id, col2) values (null, 'Bright');


-- 4.4 copying rows from one table to another

insert into dept_east (deptno, dname, loc)
select deptno, dname, loc
  from dept
where loc in ('NEW YORK', 'BOSTON');


-- 4.5 copying a table definition

create table dept_2 as
select * from dept
where 1 = 0; -- subquery that returns no rows


-- 4.6 inserting into multiple tables at once

-- not possible in Postgres


-- 4.7 blocking inserts to certain columns

-- create a view exposing only the desired columns

create view new_emps as
select empno, ename, job
from emp;

-- then insert into this view


-- 4.8 modifying records

update emp
set sal = sal * 1.1
where deptno = 20;


-- 4.9 updating when corresponding rows exist

update emp
set sal = sal * 1.2
where empno in (select empno from emp_bonus);


-- 4.10 updating with values from another table

-- with new_sal as:
-- deptno | sal
--     10 | 4000

update emp
set sal = ns.sal,
comm = ns.sal / 2
from new_sal ns
where ns.deptno = emp.deptno;


-- 4.11 Merging records

merge into emp_commission ec
using(select * from emp) emp
on ec.empno = emp.empno
when matched then
  update set ec.comm = 1000
  delete where (sal < 2000)
when not matched then
  insert (ec.empno, ec.ename, ec.deptno, ec.comm)
  values (emp.empno, emp.ename, emp.deptno, emp.comm);


-- 4.12 deleting all records

delete from tbl;

truncate tbl; -- cannot be undone


-- 4.13 deleting specific records

delete from emp where deptno = 99;


-- 4.14 deleting a single record

-- preferably, use the primary key

delete from emp where empno = 2222;


-- 4.15 deleting referential integrity violations

-- delete employees assigned to departments that do not exist

delete from emp
where not exists (
  select * from dept
  where dept.deptno = emp.deptno
);


-- 4.16 deleting duplicate records

delete from dupes
where id not in (select min(id)
                 from dupes
                 group by name);


-- 4.17 deleting records referenced from another table

delete from emp
where deptno in (select deptno
  from dept_occurrences
  group by deptno
  having count(*) >= 3);


-- 4.18 Warnings

always preview any data you intend to update or delete
