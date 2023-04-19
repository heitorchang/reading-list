-- 5.1 Listing tables

select table_name from information_schema.tables
where table_schema = 'public';


-- 5.2 listing columns

select column_name, data_type, ordinal_position
from information_schema.columns
where table_schema = 'public'
and table_name = 'emp';


-- 5.3 listing indexed columns

select a.tablename, a.indexname, b.column_name
from pg_catalog.pg_indexes a,
  information_schema.columns b
where a.schemaname = 'public'
  and a.tablename = 'emp';

-- Huh? there are 1800+ rows


-- 5.4 Listing constraints on a table
--SKIP--


-- 5.5 listing foreign keys without corresponding indexes
--SKIP--


-- 5.6 Using SQL to generate SQL (dynamic SQL statements)

select 'select count(*) from ' || table_name || ';' cnts
from (
  select table_name from information_schema.tables
  where table_schema = 'public'
) x;


-- 5.7 describing the data dictionary views in Oracle
--SKIP--
