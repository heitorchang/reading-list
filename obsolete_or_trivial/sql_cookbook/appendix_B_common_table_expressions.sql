-- double aggregate with subquery

select max(head_count) as highest_head_count from
  (select job, count(empno) as head_count
   from emp
   group by job) x;


-- enabling recursion was the main inspiration for CTEs

-- PostgreSQL docs example

WITH regional_sales AS (
    SELECT region, SUM(amount) AS total_sales
    FROM orders
    GROUP BY region
), top_regions AS (
    SELECT region
    FROM regional_sales
    WHERE total_sales > (SELECT SUM(total_sales)/10 FROM regional_sales)
)
SELECT region,
       product,
       SUM(quantity) AS product_units,
       SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions)
GROUP BY region, product;


It is possible to define the column names of the CTE:

with head_count_tab (job, head_count) as (
  select job, count(empno)
  from emp
  group by job
)
select max(head_count) as highest_job_count
from head_count_tab;


-- fibonacci

-- Python
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


with recursive working_table (a, b, index1) as (
  select 0, 1, 1
  union all
  select b, a + b, index1 + 1
  from working_table
  where index1 < 20)
  select a from working_table as fib;
