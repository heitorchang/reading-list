-- 9.1 is leap year
--SKIP-- too obscure

-- idea: try to generate Feb. 29; if (Feb.) 28 appears, then it's false
select max(to_char(tmp2.dy+x.id, 'DD')) as dy
from (
select dy, to_char(dy, 'MM') as mnth
from (
select cast(cast(
date_trunc('year', current_date) as date)
+ interval '1 month' as date) as dy
from t1
) tmp1
) tmp2, generate_series(0, 29) x(id)
where to_char(tmp2.dy + x.id, 'MM') = tmp2.mnth;

-- 9.2 number of days in a year
-- idea: compute YYYY-01-01 and add 1 year, then subtract

select cur_year + interval '1 year' - cur_year
from (
select date_trunc('year', current_date)::date as cur_year
) x;


-- 9.3 extracting units of time from a date

select extract(hour from current_timestamp),
extract(minute from current_timestamp),
extract(second from current_timestamp),
extract(day from current_timestamp),
extract(month from current_timestamp),
extract(year from current_timestamp),
extract(doy from current_timestamp), -- day of year
extract(dow from current_timestamp); -- day of week

-- 9.4 first and last days of a month

select firstday, firstday + interval '1 month' - interval '1 day' as lastday
from (select date_trunc('month', current_date) as firstday) x;


-- 9.5 determine all dates for a particular weekday (e.g. all Fridays)
--SKIP-- obscure code
-- idea: generate all days of the year and keep only Fridays


-- 9.6 dates of the first and last occurrences of a specific weekday in a month
--SKIP-- too specific


-- 9.7 create a calendar
--SKIP-- ugly code


-- 9.8 list quarter start and end dates for the year
-- 01-jan to 31-mar
-- 01 apr to 30-jun
-- etc.

-- using a recursive CTE

with recursive x (dy, cnt) as
(select date_trunc('year', current_date)::date as dy, id
from t1
union all
select cast(dy + interval '3 months' as date), cnt + 1
from x
where cnt + 1 <= 4 -- recursion end
)
select dy as qstart, (dy + interval '3 months' - interval '1 day')::date as qend from x;


-- 9.9 determining quarter start and end dates for a given quarter
--SKIP-- too specific
-- 2022Q1
-- using integer division
select (extract(year from '2022-12-01'::date))::text || 'Q' || (extract(month from '2022-12-01'::date)::integer - 1) / 3 + 1;


-- 9.10 filling in missing dates
-- alternative solution (no recursive CTE)

with first_of_mo as (
select d from generate_series('2006-01-01'::date, '2006-12-31'::date, '1 month') as t(d)
)
select first_of_mo.d, count(hiredate)
from first_of_mo
left join emp on extract(month from d) = extract(month from hiredate)
and extract(year from d) = extract(year from hiredate)
group by d
order by d;


-- 9.11 searching on specific units of time

select ename
from emp
where rtrim(to_char(hiredate, 'month')) in ('february', 'december')
or rtrim(to_char(hiredate, 'day')) = 'tuesday';


-- 9.12 comparing records using specific parts of a date

select a.ename || ' was hired on the same month as ' || b.ename as msg
from emp a, emp b
where to_char(a.hiredate, 'month') = to_char(b.hiredate, 'month')
and a.empno < b.empno; -- needed to filter out duplicates


-- 9.13 identifying overlapping date ranges

-- trick: self-join
-- suppose emp_project is
ename. proj_id,  proj_start, proj_end
CLARK        1  16-JUN-2005  18-JUN-2005
...

create table emp_project (
  proj_id integer primary key,
  ename text,
  proj_start date,
  proj_end date
);

insert into emp_project (proj_id, ename, proj_start, proj_end) values
(2, 'KING', '17-jun-2005', '21-jun-2005'),
(8, 'KING', '23-jun-2005', '25-jun-2005'),
(14, 'KING', '29-jun-2005', '30-jun-2005'),
(11, 'KING', '26-jun-2005', '27-jun-2005'),
(5, 'KING', '20-jun-2005', '24-jun-2005');

select a.ename,
'project ' || b.proj_id || ' overlaps project ' || a.proj_id as msg
from emp_project a, emp_project b
where a.ename = b.ename
and b.proj_start >= a.proj_start
and b.proj_start <= a.proj_end
and a.proj_id != b.proj_id;
