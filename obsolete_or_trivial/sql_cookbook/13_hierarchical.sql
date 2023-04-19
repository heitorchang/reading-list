-- 13.1 expressing parent-child relationship

select c.ename || ' works for ' || p.ename
from emp c, emp p
where c.mgr = p.empno;


-- 13.2 child-parent-grandparent relationship

with recursive x (tree, mgr, depth) as ( select ename, mgr, 0 from emp
--where ename = 'MILLER'
union all
select x.tree || '->' || e.ename, e.mgr, x.depth + 1
from emp e, x
where x.mgr = e.empno
)
select tree from x
where depth = 2;


-- 13.3 hierarchical view

with recursive x (ename, empno) as (
  select ename, empno
  from emp
  where mgr is null
  union all
  select x.ename || '->' || e.ename,
  e.empno
  from emp e, x
  where e.mgr = x.empno
)
select ename as emp_tree
from x
order by ename;


-- 13.4 find all child rows for a given parent

-- find those who work for JONES
with recursive x (ename, empno) as (
  select ename, empno
  from emp
  where ename = 'JONES'
  union all
  select e.ename, e.empno
  from emp e, x
  where e.mgr = x.empno
)
select ename
from x;


-- 13.5 determine which rows are leaf, branch, or root nodes
--SKIP-- too specific
