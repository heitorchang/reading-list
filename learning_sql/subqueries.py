# self-contained subqueries are "noncorrelated"
# if a subquery references columns from the containing statement, it is "correlated"

def in_operator():
    q("""SELECT branch_id, name, city
    FROM branch
    WHERE name IN ('Headquarters', 'Quincy Branch')""")

def employees_who_supervise_others():
    q("""SELECT emp_id, fname, lname, title
    FROM employee
    WHERE emp_id IN (SELECT superior_emp_id
    FROM employee)""")

def emp_do_not_supervise():
    # The opposite is NOT IN

    q("""SELECT fname, lname, title
    FROM employee
    WHERE emp_id NOT IN (SELECT superior_emp_id FROM employee WHERE superior_emp_id IS NOT NULL)""")

    # IS NOT NULL is needed because when comparing a valid value to NULL results in 'unknown'

def accts_smaller_bal():
    q("""SELECT account_id, cust_id, product_cd, avail_balance
    FROM account
    WHERE avail_balance < ALL (SELECT a.avail_balance
    FROM account AS a INNER JOIN individual AS i
    ON a.cust_id = i.cust_id
    WHERE i.fname = 'Frank' AND i.lname = 'Tucker');""")

    # avail_balance > ANY will work if the account exceeds any of the subquery's accounts.

def multiple_simple_subqueries():
    q("""SELECT account_id, product_cd, cust_id
    FROM account
    WHERE open_branch_id = (SELECT branch_id
    FROM branch
    WHERE name = 'Woburn Branch')
    AND open_emp_id IN (SELECT emp_id
    FROM employee
    WHERE title LIKE '%Teller');""")

def multi_column_subquery():
    q("""
    SELECT account_id, cust_id
    FROM account
    WHERE (open_branch_id, open_emp_id) IN
    (SELECT b.branch_id, e.emp_id
    FROM branch AS b INNER JOIN employee AS e
    ON b.branch_id = e.assigned_branch_id
    WHERE b.name = 'Woburn Branch'
    AND e.title LIKE '%Teller')""")

def count_num_accts():
    q("""SELECT COUNT(*) AS ct FROM account AS a""")

def correlated_subquery_two_accts():
    q("""SELECT c.cust_id, c.city
    FROM customer AS c
    WHERE (SELECT COUNT(*) FROM account AS a
    WHERE a.cust_id = c.cust_id) = 2;""")

    # WHERE (SELECT SUM(avail_balance) WHERE a.cust_id = c.cust_id)
    # BETWEEN 5000 AND 10000

    # The correlated subquery is executed once per customer

def exists():
    # EXISTS identifies that a relationship exists, without regard to quantity
    # By convention, use SELECT 1
    
    q("""SELECT a.account_id, a.avail_balance
    FROM account AS a
    WHERE EXISTS (SELECT 1
    FROM transaction AS t
    WHERE t.account_id = a.account_id
    AND t.txn_date = '2008-06-30');""")

def not_exists():
    # Check that a subquery returns no rows

    # a roundabout way of finding nonbusiness customers
    q("""SELECT a.account_id, a.cust_id
    FROM account AS a
    WHERE NOT EXISTS (SELECT 1
    FROM business AS b
    WHERE b.cust_id = a.cust_id);""")

def subquery_as_data_source():
    q("""SELECT d.dept_id, d.name, e_cnt.how_many AS num_emp
    FROM department AS d INNER JOIN
    (SELECT dept_id, COUNT(*) AS how_many
    FROM employee GROUP BY dept_id) AS e_cnt
    ON d.dept_id = e_cnt.dept_id;""")

def cust_rollup():
    q("""SELECT SUM(a.avail_balance) AS bal
    FROM account AS a
    INNER JOIN product AS p
    ON a.product_cd = p.product_cd
    AND p.product_type_cd = 'ACCOUNT'
    GROUP BY a.cust_id""")

def customer_groups():
    q("""
    SELECT groups.name, COUNT(*) num_customers
    FROM
    (SELECT SUM(a.avail_balance) AS cust_balance
    FROM account AS a INNER JOIN product AS p
    ON a.product_cd = p.product_cd
    WHERE p.product_type_cd = 'ACCOUNT'
    GROUP BY a.cust_id) AS cust_rollup
    INNER JOIN
    (SELECT 'Small Fry' AS name, 0 AS low_limit, 4999.99 AS high_limit
    UNION ALL
    SELECT 'Average Joes' AS name, 5000 AS low_limit, 9999.99 AS high_limit
    UNION ALL
    SELECT 'Heavy Hitters' AS name, 10000 AS low_limit, 99999999.99 AS high_limit) AS groups
    ON cust_rollup.cust_balance BETWEEN groups.low_limit AND groups.high_limit
    GROUP BY groups.name""")
    
def data_report():
    # p. 176
    q("""SELECT p.name AS product, b.name AS branch,
    e.fname AS emp_name, acct_groups.tot_dep  AS tot_dep
    FROM
    (SELECT product_cd, open_branch_id AS branch_id, open_emp_id AS emp_id,
    SUM(avail_balance) AS tot_dep
    FROM account
    GROUP BY product_cd, branch_id, emp_id) AS acct_groups
    INNER JOIN employee AS e ON e.emp_id = acct_groups.emp_id
    INNER JOIN branch AS b ON b.branch_id = acct_groups.branch_id
    INNER JOIN product AS p ON p.product_cd = acct_groups.product_cd
    WHERE p.product_type_cd = 'ACCOUNT';""")

def subquery_filter():
    q("""SELECT open_emp_id, COUNT(*) AS how_many
    FROM account
    GROUP BY open_emp_id
    HAVING COUNT(*) = (SELECT MAX(emp_cnt.how_many)
    FROM (SELECT COUNT(*) AS how_many
    FROM account
    GROUP BY open_emp_id) emp_cnt)""")

def subquery_order_by():
    q("""SELECT emp.emp_id, emp.lname AS emp_lname,
    (SELECT boss.lname AS boss_lname FROM employee AS boss
    WHERE boss.emp_id = emp.superior_emp_id) AS boss_name
    FROM employee AS emp
    WHERE emp.superior_emp_id IS NOT NULL
    ORDER BY (SELECT boss.lname FROM employee AS boss
    WHERE boss.emp_id = emp.superior_emp_id), emp.lname;
    """)

# Subqueries may be used as data sources in INSERT statements; however, if an
# error occurs, NULL will be inserted if allowed.

def test_your_knowledge_1():
    q("""
    SELECT account_id, product_cd, cust_id, avail_balance
    FROM account
    WHERE product_cd IN
    (SELECT product_cd FROM product WHERE product_type_cd = 'LOAN')
    """)

def test_your_knowledge_2():
    q("""
    SELECT a.account_id, a.product_cd, a.cust_id, a.avail_balance
    FROM account AS a
    WHERE EXISTS (SELECT 1
    FROM product AS p
    WHERE a.product_cd = p.product_cd AND
    p.product_type_cd = 'LOAN')""")
