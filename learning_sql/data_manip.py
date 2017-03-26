string_notes = """

Strings p. 113

entering single quotes :
'this string didn''t work'

SELECT quote(s) FROM string_tbl;

CHAR(129)

ASCII('ó')

LENGTH(vchar_fld)

POSITION('characters' IN char_fld)  # returns 0 if nothing was found

LOCATE('is', vchar_fld, 5)

strcmp(a, b)  returns -1 if a is before b in sort order, 0 if identical and 1 if a comes after b

CONCAT(a, ' ', b)

INSERT(orig_str, position_to_start, chars_to_replace (or 0), replacement_str)

SUBSTRING(str, position_to_start, num_chars)

"""

numbers_notes = """

p. 126
MOD(), CEIL(), FLOOR(), (),

temporal_notes = """

p. 130

SELECT CAST('2001-01-01' AS DATE)
CAST ('2014-03-02 15:30:00' AS DATETIME)
CAST ('109:02:23' AS TIME)

STR_TO_DATE('September 23, 2009', '%M %d, %Y')

CURRENT_DATE(), CURRENT_TIME(), CURRENT_TIMESTAMP()

DATE_ADD(CURRENT_DATE(), INTERVAL 5 DAY)

LAST_DAY('2008-09-17') -> 2008-09-30

DAYNAME('2008-09-19') -> "Thursday"

EXTRACT(YEAR FROM '2009-02-01 23:23:23')

DATEDIFF(a, b)

CAST('12345' AS SIGNED INTEGER)

"""
