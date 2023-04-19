-- 8.1 adding/subtracting days, months, years

select empno, hiredate + interval '5 days' as d1,
hiredate - interval '5 months' as d2,
hiredate + interval '5 years' as d3
from emp
where deptno = 10;


-- 8.2 determining the number of days between two dates

select ward_hd - allen_hd
from (select hiredate as ward_hd from emp where ename = 'WARD') x,
(select hiredate as allen_hd from emp where ename = 'ALLEN') y;
-- answer: 2


-- 8.3 number of business days between two dates
--WARNING-- book code looks buggy, should not be 30 because the dates are a bit below one calendar month
-- PROBLEM: holidays: keep a separate table that identifies holidays

-- idea: use dow to filter out weekends

-- use the T500 pivot table to generate days between two dates, then count each day that is not a weekend

select sum(case when trim(to_char(jones_hd + t500.id - 1, 'day'))
            in ('SATURDAY', 'SUNDAY')
           then 0 else 1
           end) as days
from (
    select max(case when ename = 'BLAKE'
               then hiredate
               end) as blake_hd,
    max(case when ename = 'JONES'
    then hiredate end) as jones_hd
    from emp
    where ename in ('BLAKE', 'JONES')
    ) x,
    t500 where t500.id <= blake_hd - jones_hd + 1;


-- 8.4 number of months or years between two dates

select mnth, mnth / 12 as yr
from (
select (extract(year from max_hd) -
extract(year from min_hd)) * 12 +
(extract(month from max_hd) -
extract(month from min_hd)) as mnth
from (
select min(hiredate) as min_hd, max(hiredate) as max_hd
from emp
) x
) y;


-- 8.5 number of seconds, mins, hrs between two dates

select dy*24 as hr, dy*24*60 as min, dy*24*60*60 as sec
from (
select (max(case when ename = 'WARD' then hiredate end) - max(case when ename = 'ALLEN' then hiredate end)) as dy
from emp
) x;


-- 8.6 counting the occurrences of weekdays in a year

-- use generate_series to generate one row for every day in the year

select to_char(cast(date_trunc('year', current_date) as date) + gs.id - 1, 'DAY'),
count(*) from generate_series(1, 366) gs(id)
where gs.id <= (cast (date_trunc('year', current_date) +
interval '12 months' as date) -
cast(date_trunc('year', current_date) as date))
group by to_char(
cast(date_trunc('year', current_date) as date) + gs.id - 1, 'DAY');


-- 8.7 date difference between current record and next record
-- use LEAD window function

select x.*, x.next_hd - x.hiredate as diff
from (
select e.deptno, e.ename, e.hiredate,
lead(hiredate) over (order by hiredate) as next_hd
from emp e
where e.deptno = 10
) x;
