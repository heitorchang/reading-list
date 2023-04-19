-- 10.1 locate range of consecutive values

-- return projects where proj_end equals proj_start of the next row

select proj_id, proj_start, proj_end
from (
select proj_id, proj_start, proj_end,
lead(proj_start) over (order by proj_id) next_proj_start
from V
) alias
where next_proj_start = proj_end;


-- 10.2 differences between rows in the same group/partition

with next_sal_tab as (
select deptno, ename, sal, hiredate, lead(sal) over (partition by deptno order by hiredate) as next_sal
from emp)
select deptno, ename, sal, hiredate, coalesce(cast(sal - next_sal as text), 'N/A') as diff
from next_sal_tab;


-- 10.3 locating the beginning and end of a range of consecutive values

select proj_grp, min(proj_start), max(proj_end)
from (
select proj_id, proj_start, proj_end,
sum(flag) over (order by proj_id) proj_grp
from (
select proj_id, proj_start, proj_end,
case when
lag(proj_end) over (order by proj_id) = proj_start
then 0 else 1
end flag
from V
) a1
) a2
group by proj_grp;


-- 10.4 filling in missing values in a range of values

select y.yr, coalesce(x.cnt, 0) as cnt
from (
  select min_year - mod(cast(min_year as integer), 10) + rn as yr
  from (
    select (select min(extract(year from hiredate))
            from emp) as min_year,
            id - 1 as rn
            from t10
           ) a
       ) y
    left join
    (
      select extract(year from hiredate) as yr, count(*) as cnt
      from emp
      group by extract(year from hiredate)
    ) x
on (y.yr = x.yr);


-- generate_series solution

with yrs as (
select generate_series(2000, 2009) as i
)
select yrs.i, count(hiredate) from yrs
left join emp on extract(year from hiredate) = i
group by i
order by i;


-- 10.5 generating consecutive numeric values

select i from generate_series(0, 20, 2) as g(i); -- 11 rows
