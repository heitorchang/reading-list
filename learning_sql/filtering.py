def not_operator():
    print_simple_query(cnx, """
    SELECT fname, lname
    FROM employee
    WHERE end_date IS NULL
    AND NOT (title = 'Teller' OR start_date < '2007-01-01')
    """)

def is_not():
    # usage of != operator; <> is equivalent
    
    print_simple_query(cnx, """
    SELECT fname, lname
    FROM employee
    WHERE end_date IS NULL
    AND title != 'Teller' AND start_date >= '2007-01-01'""")

def join_condition():
    print_simple_query(cnx, """
    SELECT pt.name AS product_type, p.name AS product
    FROM product AS p INNER JOIN product_type AS pt
    ON p.product_type_cd = pt.product_type_cd
    WHERE pt.name <> 'Customer Accounts';""")

    # WHERE pt.name = 'Customer Accounts';""")

def between():
    # endpoints are inclusive, id 1 (Michael) is included
    
    print_simple_query(cnx, """
    SELECT emp_id, fname
    FROM employee
    WHERE start_date BETWEEN '2005-06-22' AND '2007-01-01'""")

def membership():
    print_simple_query(cnx, """
    SELECT account_id, product_cd, avail_balance
    FROM account
    WHERE product_cd NOT IN ('CHK', 'SAV', 'CD', 'MM');""")

def subquery():
    print_simple_query(cnx, """
    SELECT account_id, product_cd, avail_balance
    FROM account
    WHERE product_cd IN (SELECT product_cd FROM product
      WHERE product_type_cd = 'ACCOUNT');""")

def wildcard():
    # _ for a single character, % zero or more
    
    print_simple_query(cnx, """
    SELECT fname, lname FROM employee
    WHERE lname LIKE '_a%e%';""")

def regexp():
    print_simple_query(cnx, """
    SELECT emp_id, fname, lname
    FROM employee
    WHERE lname REGEXP '^[FG]';""")

def is_not_null():
    print_simple_query(cnx, """
    SELECT emp_id, fname, lname
    FROM employee
    WHERE superior_emp_id IS NOT NULL;""")

def null_pitfall():
    # != will not return rows where the column is NULL
    print_simple_query(cnx, """
    SELECT emp_id, fname, lname, superior_emp_id
    FROM employee
    WHERE superior_emp_id != 6 OR superior_emp_id IS NULL;""")
