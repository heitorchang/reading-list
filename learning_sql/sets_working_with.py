def union_all():
    # UNION combines and removes duplicates, UNION ALL merely appends rows
    global_cnx("""
    SELECT 'IND' AS type_cd, cust_id, lname AS name
    FROM individual
    UNION ALL
    SELECT 'BUS' AS type_cd, cust_id, name
    FROM business;""")

def intersect():
    # Not available in MySQL
    global_cnx("""
    SELECT emp_id, fnmae, lname
    FROM employee
    INTERSECT
    SELECT cust_id, fname, lname
    FROM individual;""")

def simulate_intersect():
    global_cnx("""
    SELECT emp_id
    FROM employee
    WHERE title LIKE "%Teller"
    AND assigned_branch_id = 2
    AND emp_id IN (
    SELECT DISTINCT open_emp_id
    FROM account
    WHERE open_branch_id = 2);""")

def simulate_except():
    global_cnx("""
    SELECT emp_id
    FROM employee
    WHERE assigned_branch_id = 2
    AND (title LIKE '%Teller')
    AND emp_id NOT IN (SELECT DISTINCT open_emp_id
    FROM account
    WHERE open_branch_id = 2);""")
