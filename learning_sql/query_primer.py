# p. 42

def query_lname(cnx):
    cursor = cnx.cursor()
    lname_sql = """
    SELECT emp_id, fname, lname
    FROM employee
    WHERE lname = 'Grossman';
    """

    cursor.execute(lname_sql)
    for row in cursor:  # row is a tuple
        print(type(row))
        print(row)

    cursor.close()

def query_all_depts(cnx):
    cursor = cnx.cursor()
    depts_sql = """
    SELECT *
    FROM department;
    """

    cursor.execute(depts_sql)
    for row in cursor:
        print(row)

    cursor.close()

def select_literals(cnx):
    # defined column names appear as tuple field names
    cursor = cnx.cursor(named_tuple=True)
    literals_sql = """
    SELECT emp_id,
    'Active',
    emp_id * 3.1415 AS emp_id_x_pi,
    UPPER(lname) AS lname_upper
    FROM employee;
    """
    
    cursor.execute(literals_sql)
    for row in cursor:
        print(row)
    cursor.close()

def select_distinct(cnx):
    # Avoid DISTINCT in general, because it requires data to be sorted
    cursor = cnx.cursor()
    not_distinct_sql = """
    SELECT cust_id
    FROM account;
    """
    # cursor.execute(not_distinct_sql)

    distinct_sql = """
    SELECT DISTINCT cust_id
    FROM account;
    """
    cursor.execute(distinct_sql)

    for row in cursor:
        print(row)

    cursor.close()

def subquery_name(cnx):
    cursor = cnx.cursor()
    subquery_sql = """
    SELECT e.emp_id, e.fname
    FROM (SELECT emp_id, fname, lname, start_date, title
          FROM employee) AS e;
    """
    cursor.execute(subquery_sql)
    for row in cursor:
        print(row)
    cursor.close()

def create_employee_view(cnx):
    """A view is a virtual table, with uses including hiding columns
    and simplifying complex database designs."""
    
    cursor = cnx.cursor()
    view_sql = """
    CREATE VIEW employee_vw AS
    SELECT emp_id, fname, lname, YEAR(start_date) AS start_year
    FROM employee;
    """
    cursor.execute(view_sql)
    cursor.close()

def select_from_view(cnx):
    cursor = cnx.cursor()
    select_sql = """
    SELECT emp_id, start_year
    FROM employee_vw;
    """
    cursor.execute(select_sql)
    for row in cursor:
        print(row)
    cursor.close()

# p. 51
def table_links(cnx):
    cursor = cnx.cursor(named_tuple=True)
    link_sql = """
    SELECT e.emp_id, e.fname, e.lname, d.name as dept_name
    FROM employee AS e INNER JOIN department AS d
    ON e.dept_id = d.dept_id
    ORDER BY e.emp_id;
    """
    cursor.execute(link_sql)
    for row in cursor:
        print(row)
    cursor.close()

def where_and(cnx):
    cursor = cnx.cursor()
    # other operators include OR and NOT
    head_teller_start = """
    SELECT emp_id, fname, start_date, title
    FROM employee
    WHERE title = 'Head Teller'
    AND start_date > '2006-01-01';
    """
    cursor.execute(head_teller_start)
    for row in cursor:
        print(row)
    cursor.close()

def where_group_cond(cnx):
    cursor = cnx.cursor()
    teller_2006_or_2007 = """
    SELECT emp_id, fname, lname, start_date, title
    FROM employee
    WHERE (title = 'Head Teller' AND start_date > '2006-01-01')
    OR (title = 'Teller' AND start_date > '2007-01-01');
    """
    cursor.execute(teller_2006_or_2007)
    for row in cursor:
        print(row)
    cursor.close()

def group_by_emp_count(cnx):
    cursor = cnx.cursor()
    dept_num_emp = """
    SELECT d.name, count(e.emp_id) AS num_emp, d.dept_id
    FROM department AS d INNER JOIN employee AS e
    ON d.dept_id = e.dept_id
    GROUP BY d.name
    HAVING num_emp > 2;
    """
    cursor.execute(dept_num_emp)
    for row in cursor:
        print(row)
        
    cursor.close()

# p. 60
def test_your_knowledge(cnx):
    cursor = cnx.cursor(named_tuple=True)

    ANSWER = """
    /* 3.1 */
    SELECT emp_id, fname, lname
    FROM employee
    ORDER BY lname, fname;
    """

    ANSWER = """
    /* 3.2 */
    SELECT account_id, cust_id, avail_balance
    FROM account
    WHERE status = 'ACTIVE' AND avail_balance > 2500;
    """

    ANSWER = """
    /* 3.3 */
    SELECT DISTINCT open_emp_id
    FROM account;
    """

    ANSWER = """
    /* 3.4 */
    SELECT p.product_cd, a.cust_id, a.avail_balance
    FROM product AS p INNER JOIN account AS a
    ON p.product_cd = a.product_cd
    WHERE p.product_type_cd = 'ACCOUNT'
    ORDER BY p.product_cd, a.cust_id;
    """
    cursor.execute(ANSWER)
    for row in cursor:
        print(row)
    cursor.close()
