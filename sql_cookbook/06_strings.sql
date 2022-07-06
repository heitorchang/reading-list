-- 6.1 walking a string

-- original
select substr(e.ename, iter.pos, 1) as c
  from (select ename from emp where ename = 'KING') e,
  (select id as pos from t10 order by id) iter
where iter.pos <= length(e.ename);

-- better (uses generate_series)
select substr(e.ename, iter.pos, 1) as c
  from (select ename from emp where ename = 'KING') e,
  (select generate_series(1, 10) as pos) iter -- large enough limit
where iter.pos <= length(e.ename);

-- cumulative substrings
select substr(e.ename, iter.pos) a,
  substr(e.ename, length(e.ename) - iter.pos + 1) b
  from (select ename from emp where ename = 'KING') e,
  (select generate_series(1, 10) as pos) iter -- large enough limit
where iter.pos <= length(e.ename);


-- CTE solution that does not depend on T10 pivot table or hardcoded
--   constants
with ename_cte as (
	select ename, max(length(ename)) as emax from emp where ename in ('KING', 'CLARK')
	group by ename
), iter as (
    select generate_series(1, max(length(ename))) as pos
	from ename_cte
)
select pos, substr(e.ename, iter.pos, 1) as c
from ename_cte e, iter
where iter.pos <= length(e.ename)
group by iter.pos, e.ename
order by e.ename, pos;


-- 6.2 embedding quotes in string literals

use '', for example: select 'g''day mate' qmarks from t1;
The string literal '' in NULL


-- 6.3 counting the occurrences of a character

-- suppose you have '10,clark,manager'. How many commas are there?

select (length('10,clark,manager') -
        length(replace('10,clark,manager', ',', ''))) / length(',')
        as cnt
from t1;

-- division by the length of the string searched is needed, otherwise the
-- number of characters will be returned.


-- 6.4 remove unwanted characters

-- example: remove vowels and zeros

select ename,
replace(translate(ename, 'AEIOU', 'aaaaa'), 'a', '') as stripped1,
sal,
replace(sal::text, '0', '') as stripped2
from emp;


-- 6.5 separate numeric from character data

-- use TRANSLATE to transform multiple characters into a single character you can reference

select replace(
  translate(data, '0123456789', '0000000000'), '0', '') as ename,
    cast(
      replace(
        translate(lower(data), 'qwertyuiopasdfghjklzxcvbnm', rpad('', 26, 'z')), 'z', '') as integer) as sal
from (
  select ename || sal as data
  from emp
) x;


-- 6.6 determine if string is alphanumeric
-- idea: non-alphanumeric chars will not become *, so return only
-- the rows where all chars were valid.

select data
from V6_6
where translate(lower(data),
  '1234567890qwertyuiopasdfghjklzxcvbnm', rpad('', 36, '*')) = rpad('', length(data), '*');


-- 6.7 extract initials from a name

-- first, replace lowercase letters with # then remove them

select replace(
  translate('Joe Montana', 'qwertyuiopasdfghjklzxcvbnm', rpad('', 26, '#')), '#', '');

-- then replace the space with . and add a final . (with || '.')


-- 6.8 ordering by parts of a string

select ename from emp
order by substr(ename, length(ename) - 1); -- sorts by last two letters


-- 6.9 ordering by a number in a string
--SKIP--

-- idea: use REPLACE and TRANSLATE to remove nondigits, then cast digits as a number


-- 6.10 creating a comma-separated list from table rows

select deptno,
  string_agg(ename, ',' order by ename) as emps
from emp
group by deptno;


-- 6.11 convert delimited data into a multivalued in-list
--SKIP--

-- obscure, idea is to use SPLIT_PART to parse the string
-- 1. pad string with ',' || s || ','
-- 2. select split_part


-- 6.12 to 6.15
--SKIP--


-- 6.17 finding text not matching a pattern
--SKIP--

-- general regexp function
select empno from emp where empno::text similar to '7[0-9][0-5]{2}';
