def acct_business():
    q("""
    SELECT a.account_id, a.cust_id, b.name
    FROM account a LEFT OUTER JOIN business b
    ON a.cust_id = b.cust_id ORDER BY account_id""")

def three_way_outer_join():
    q("""SELECT a_i.account_id, a_i.product_cd,
    a_i.person_name, b.name AS business_name
    FROM
    (SELECT a.account_id, a.product_cd, a.cust_id,
    CONCAT(i.fname, ' ', i.lname) AS person_name
    FROM account a LEFT OUTER JOIN individual i
    ON a.cust_id = i.cust_id) AS a_i
    LEFT OUTER JOIN business b
    ON a_i.cust_id = b.cust_id
    ORDER BY a_i.account_id;""")

def employee_and_supervisor():
    # Previously, an INNER JOIN was used:
    q("""SELECT e.fname, e.lname, mgr.fname AS mgr_fname, mgr.lname AS mgr_lname
    FROM employee AS e LEFT OUTER JOIN employee AS mgr
    ON e.superior_emp_id = mgr.emp_id;""")

def cross_join():
    q("""SELECT p.name AS p_name, p.product_cd, pt.name AS pt_name
    FROM product AS p CROSS JOIN product_type AS pt ORDER BY p_name, product_cd""")

def test_your_knowledge_1():
    q("""
    SELECT p.name AS product_name, a.account_id AS acct_id
    FROM product AS p LEFT OUTER JOIN account AS a
    ON p.product_cd = a.product_cd""")

def test_your_knowledge_3():
    q("""
    SELECT a.account_id, a.product_cd, i.fname, i.lname, b.name
    FROM account a LEFT OUTER JOIN business AS b
    ON a.cust_id = b.cust_id
    LEFT OUTER JOIN individual AS i
    ON a.cust_id = i.cust_id
    ORDER BY a.account_id;""")
