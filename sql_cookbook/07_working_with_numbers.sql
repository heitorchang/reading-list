-- 7.1 average

select avg(sal) as avg_sal from emp;

select deptno, avg(sal) as avg_sal
from emp
group by deptno;

-- if including nulls
select avg(coalesce(sal, 0)) from emp;


-- 7.2 finding min/max

select min(sal) as min_sal, max(sal) as max_sal
from emp;

select deptno, min(comm), max(comm)
from emp
group by deptno;

-- 7.3 summing values

select deptno, sum(sal) as total_for_dept
from emp
group by deptno;


-- 7.4 count rows

select count(*) from emp;


-- 7.5 counting values in a column

-- use a column name instead of *

select count(comm) from emp;


-- 7.6 running total

select ename, sal, sum(sal) over (order by sal, empno) as running_total
-- empno is needed to avoid duplicate additions
from emp
order by running_total;


-- WARNING: WRONG! duplicate salaries are added twice
select ename, sal, sum(sal) over (order by sal) as running_total
from emp
order by running_total;


-- 7.7 running product
-- Note: uses a mathematical trick

select empno, ename, sal, exp(sum(ln(sal)) over (order by sal, empno)) as running_prod
from emp
where deptno = 10;
-- WARNING: breaks when there are 0s


-- 7.8 smoothing a series of values

create table sales (
  sale_id integer primary key,
  date1 date,
  sales integer
);

insert into sales (sale_id, date1, sales)
values
(1, '2020-01-01', 647),
(2, '2020-01-02', 561),
(3, '2020-01-03', 741),
(4, '2020-01-04', 978),
(5, '2020-01-05', 1062),
(6, '2020-01-06', 1072);


with cte as (
  select date1, sales, lag(sales, 1) over (order by date1) as lag1,
  lag(sales, 2) over (order by date1) as lag2
  from sales
)
select date1, (sales + lag1 + lag2) / 3.0 as moving_avg from cte;

-- opposite of LAG (preceding rows) is LEAD (following rows)

-- with a window function

select date1, sum(sales) over (order by date1 rows between 2 preceding and current row) / 3.0 as moving_avg
from sales;


-- 7.9 calculating a mode

select sal from (
  select sal, dense_rank() over (order by cnt desc) as rnk
  from (
    select sal, count(*) as cnt
    from emp
    where deptno = 20
    group by sal
  ) x
) y
where rnk = 1;


-- 7.10 Median

select percentile_cont(0.5) within group (order by sal)
from emp
where deptno = 20;


-- with cte
with indexed as (
  select (row_number() over (order by sal)) - 1 as idx, sal from emp
  where deptno = 10
), row_ct as (
  select count(*) as max_idx from emp
  where deptno = 10
), odd_even as (
  select mod(row_ct.max_idx, 2) as odd_even
  from row_ct
), odd_even_cases as (
  select indexed.sal as result, 1 as is_odd, max_idx from indexed, row_ct where idx = max_idx / 2
  union all
  select sum(indexed.sal) / 2.0 as result, 0 as is_odd, max_idx from indexed, row_ct where idx in (max_idx / 2, max_idx / 2 + 1)
  group by max_idx
)
select odd_even_cases.result from odd_even_cases, odd_even where is_odd = odd_even.odd_even;

-- NOTE:
-- variables can be defined in subqueries
select (select count(*) from emp) as total, (select mod(count(*), 2) from emp) as is_odd;


-- 7.11 percentage of a total

-- my window function (DO NOT GROUP BY at the end!)
select deptno, sum(sal) over (partition by deptno) as dept_sal, 100.0 * sum(sal) over (partition by deptno) / sum(sal) over () as dept_pct
from emp;


-- simpler solution
select 100.0 * sum(case when deptno = 10 then sal end) / sum(sal) as pct -- 100.0 comes first to promote values to float
from emp;


-- all depts
select d1.deptno, 100.0 * sum(case when d1.deptno = e.deptno then sal end) / sum(sal) as pct
from dept d1, emp e
group by d1.deptno;


-- 7.12 aggregating nullable columns

select avg(coalesce(comm, 0)) as avg_comm
from emp
where deptno = 30;


-- 7.13 computing averages without high and low values

select avg(sal)
from emp
where sal not in (
 (select min(sal) from emp),
 (select max(sal) from emp)
);


-- 7.14 converting alphanumeric strings to numbers
select cast (
  replace(
    translate('paul123fs456', 'qwertyuiopasdfghjklzxcvbnm', rpad('', 26, '#')), '#', '')
  as integer) as num
from t1;


-- 7.15 changing values in a running total
--SKIP--

-- hypothetical credit card transaction table where PY is a payment and PR is a purchase

select case when trx = 'PY'
  then 'PAYMENT'
  else 'PURCHASE'
end trx_type, amt, sum(case when trx = 'PY' then -amt else amt end) over (order by id, amt) as balance
from V;


-- 7.16 finding outliers using median absolute deviation
--SKIP--

-- create median, deviations, and MAD CTEs, then
with median (median) as (
  select percentile_cont(0.5) within group (order by sal)
  from emp
),
devtab (deviation) as (
  select abs(sal - median)
  from emp join median on true
),
MedAbsDeviation (MAD) as (
  select percentile_cont(0.5) within group (order by deviation)
  from devtab
)
select abs(sal - median) / MAD as dev, sal, ename, job
from MedAbsDeviation, median join emp on true;


-- 7.17 Benford's Law
--SKIP--

-- too obscure
