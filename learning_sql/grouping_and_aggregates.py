# p. 143 Ch 8

def employees_opening_accounts(cnx):
    cursor = cnx.cursor()
    sql = """
    SELECT open_emp_id, COUNT(*) AS how_many
    FROM account
    GROUP BY open_emp_id
    HAVING how_many > 4;
    """
    cursor.execute(sql)

    for row in cursor:
        print(row)
    cursor.close()

def employees_names_opening_accounts(cnx):
    sql = """
    SELECT e.emp_id, e.fname, e.lname, COUNT(*) AS how_many
    FROM employee AS e INNER JOIN account AS a
    on e.emp_id = a.open_emp_id
    GROUP BY e.emp_id
    HAVING how_many > 4;
    """
    print_simple_query(cnx, sql)

def all_chk_stats(cnx):
    sql = """
    SELECT MAX(avail_balance) AS max_bal,
    MIN(avail_balance) AS min_bal,
    AVG(avail_balance) AS avg_bal,
    SUM(avail_balance) AS tot_bal,
    COUNT(*) AS num_accounts
    FROM account
    WHERE product_cd = 'CHK';
    """

    print_simple_query(cnx, sql)

# p. 147 Group by product code

def group_by_product_cd():
    print_simple_query(cnx, """
    SELECT product_cd,
      MAX(avail_balance) AS max_bal,
      MIN(avail_balance) AS min_bal,
      AVG(avail_balance) AS avg_bal,
      SUM(avail_balance) AS tot_bal,
      COUNT(*) AS num_accts
    FROM account
    GROUP BY product_cd;
    """)

# p. 151 Multicolumn Grouping

def multicolumn_grouping(): 
    print_simple_query(cnx, """
    SELECT product_cd, open_branch_id, SUM(avail_balance) AS tot_bal
    FROM account
    GROUP BY product_cd, open_branch_id;
    """)
    
def group_by_expression():
    print_simple_query(cnx, """
    SELECT EXTRACT(YEAR FROM start_date) AS year,
      COUNT(*) AS how_many
    FROM employee
    GROUP BY year;
    """)

def rollup():
    print_simple_query(cnx, """
    SELECT product_cd, open_branch_id,
      SUM(avail_balance) AS tot_bal
    FROM account
    GROUP BY product_cd, open_branch_id WITH ROLLUP;
    """)

def group_filter():
    print_simple_query(cnx, """
    SELECT product_cd, SUM(avail_balance) AS prod_bal
    FROM account
    WHERE status = 'ACTIVE'
    GROUP BY product_cd
    HAVING MIN(avail_balance) >= 1000
    AND MAX(avail_balance) <= 10000;""")

def test_your_knowledge():
    sql = """
    SELECT cust_id, COUNT(*) AS count FROM account GROUP BY cust_id
    HAVING count >= 2;
    """
    print_simple_query(cnx, sql)

def extra_credit():
    sql = """
    SELECT product_cd AS prod, open_branch_id AS branch, SUM(avail_balance) AS tot_bal
    FROM account
    GROUP BY product_cd, open_branch_id
    HAVING COUNT(*) > 1
    ORDER BY tot_bal DESC
    """

    print_simple_query(cnx, sql)
