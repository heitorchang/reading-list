# p. 81

def cartesian_product():
    # all possible combinations of employee and department
    # called a "cross join"
    
    global_cnx("""
    SELECT e.fname, e.lname, d.name
    FROM employee AS e JOIN department AS d;
    """)

def inner_join_dept_id():
    global_cnx("""
    SELECT e.fname, e.lname, d.name
    FROM employee AS e INNER JOIN department AS d
    ON e.dept_id = d.dept_id;""")

    # ON e.dept_id = d.dept_id;
    #   can be written as:
    # USING (dept_id);
    #   though it should be avoided.

def woburn_exp_tellers():
    global_cnx("""
    SELECT a.account_id, a.cust_id, a.open_date, a.product_cd
    FROM account AS a INNER JOIN employee AS e
    ON a.open_emp_id = e.emp_id
    INNER JOIN branch AS b
    ON e.assigned_branch_id = b.branch_id
    WHERE e.start_date < '2007-01-01'
    AND (e.title like '%Teller')
    AND b.name = 'Woburn Branch';""")

def join_three_tables():
    # The order of joins doesn't matter: the server picks it for you
    global_cnx("""
    SELECT a.account_id, c.fed_id, e.fname, e.lname
    FROM account AS a INNER JOIN customer AS c
    ON a.cust_id = c.cust_id
    INNER JOIN employee AS e
    ON a.open_emp_id = e.emp_id
    WHERE c.cust_type_cd = 'B';""")

def using_subqueries():
    global_cnx("""
    SELECT a.account_id, a.cust_id, a.open_date, a.product_cd
    FROM account AS a INNER JOIN
    (SELECT emp_id, assigned_branch_id
    FROM employee
    WHERE start_date < '2007-01-01'
    AND (title = 'Teller' OR title = 'Head Teller')) AS e
    ON a.open_emp_id = e.emp_id
    INNER JOIN
    (SELECT branch_id FROM branch WHERE name = 'Woburn Branch') AS b
    ON e.assigned_branch_id = b.branch_id;""")

def same_table_twice():
    # Use a different alias each time
    global_cnx("""
    SELECT a.account_id, e.emp_id, b_a.name AS open_branch,
    b_e.name AS emp_branch
    FROM account AS a INNER JOIN branch AS b_a
    ON a.open_branch_id = b_a.branch_id
    INNER JOIN employee AS e
    ON a.open_emp_id = e.emp_id
    INNER JOIN branch AS b_e
    ON e.assigned_branch_id = b_e.branch_id
    WHERE a.product_cd = "CHK" ORDER BY e.emp_id;""")

def self_join():
    # Find an employee's manager. Since the President's superior is NULL,
    # we would need an outer join (covered in Ch. 10)
    global_cnx("""
    SELECT e.fname, e.lname, e.title, e_mgr.lname AS mgr_lname
    FROM employee AS e INNER JOIN employee AS e_mgr
    ON e.superior_emp_id = e_mgr.emp_id""")
