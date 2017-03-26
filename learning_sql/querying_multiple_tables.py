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
    AND (e.title LIKE '%Teller')
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

def insert_no_fee_chk(cnx):
    cursor = cnx.cursor()
    cursor.execute("""
    INSERT INTO product (product_cd, name, product_type_cd, date_offered, date_retired)
    VALUES
    ('NFC', 'no-fee checking', 'ACCOUNT', '2006-01-01', '2006-12-31');""")
    cnx.commit()
    cursor.close()
    
def non_equi_join():
    global_cnx("""
    SELECT e.emp_id, e.fname, e.lname, e.start_date
    FROM employee AS e INNER JOIN product AS p
    ON e.start_date >= p.date_offered
    AND e.start_date <= p.date_retired
    WHERE p.name = 'no-fee checking';""")

def pair_emp():
    # using != instead of > will repeat the pair in reverse
    global_cnx("""
    SELECT e1.lname AS emp1, e2.lname AS emp2
    FROM employee AS e1 INNER JOIN employee AS e2
    ON e1.emp_id > e2.emp_id
    WHERE e1.title = 'Head Teller' AND e2.title = 'Head Teller';""");

# p. 96
def on_where_flexible():
    # SQL is flexible as to where conditions are placed (ON or WHERE)
    global_cnx("""
    SELECT a.account_id, a.product_cd, c.fed_id
    FROM account AS a INNER JOIN customer AS c
    ON a.cust_id = c.cust_id
    AND c.cust_type_cd = 'B';""")

def on_where_flexible_b():
    # SQL is flexible as to where conditions are placed (ON or WHERE)
    global_cnx("""
    SELECT a.account_id, a.product_cd, c.fed_id
    FROM account AS a INNER JOIN customer AS c
    WHERE a.cust_id = c.cust_id
    AND c.cust_type_cd = 'B';""")

def on_where_flexible_c():
    # SQL is flexible as to where conditions are placed (ON or WHERE)
    global_cnx("""
    SELECT a.account_id, a.product_cd, c.fed_id
    FROM account AS a INNER JOIN customer AS c
    ON a.cust_id = c.cust_id
    WHERE c.cust_type_cd = 'B';""")

def test_your_knowledge_1():
    global_cnx("""
    SELECT e.emp_id, e.fname, e.lname, b.name
    FROM employee AS e INNER JOIN branch AS b
    ON e.assigned_branch_id = b.branch_id;""")

def test_your_knowledge_2():
    global_cnx("""
    SELECT a.account_id, c.fed_id, p.name
    FROM account AS a INNER JOIN customer AS c
    ON a.cust_id = c.cust_id
    INNER JOIN product AS p
    ON p.product_cd = a.product_cd
    WHERE c.cust_type_cd = 'I';""")

def test_your_knowledge_3():
    # self-join
    global_cnx("""
    SELECT e.emp_id, e.fname, e.lname, e.dept_id AS e_dept, sup.dept_id AS sup_dept
    FROM employee AS e
    INNER JOIN employee AS sup
    ON e.superior_emp_id = sup.emp_id
    AND e.dept_id != sup.dept_id
    """)
