-- see also: create_tables_pivot.sql

create table dept (
deptno integer primary key,
dname text,
loc text
);

create table emp (
empno integer primary key,
ename text,
job text,
mgr integer,
hiredate date,
sal integer,
comm integer,
deptno integer references dept
);


create table emp_bonus (
  empno integer references emp,
  received date,
  type integer
);

create table emp_bonus_3_9 (
  empno integer references emp,
  received date,
  type integer
);
