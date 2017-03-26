def create_ale_account():
    # Nested accounts (for trying out self joins)
    cursor = cnx.cursor()
    cursor.execute("""
    CREATE TABLE ale_account
    (id SMALLINT UNSIGNED,
    name VARCHAR(20),
    owner SMALLINT UNSIGNED,
    sign INT,
    parent SMALLINT UNSIGNED,
    CONSTRAINT pk_name PRIMARY KEY (id),
    CONSTRAINT fk_ale_acct_owner FOREIGN KEY (owner) REFERENCES employee (emp_id))""")
    cursor.close()

def insert_ale_account(id, name, parent, sign, owner=1):
    cursor = cnx.cursor()
    sql = """
    INSERT INTO ale_account (id, name, owner, sign, parent)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id, name, owner, sign, parent))
    cnx.commit()
    cursor.close()

def populate_ale_account():
    #                        [expense at this level] (+ children)
    # expenses (200)         (+ 520 300) = 820  
    #  home (210)            [100] (+ 150 + 200 + 70) = 520
    #   groceries (211)      [90] (+ 60) = 150
    #    supermarket (2110)  50
    #    farmers mkt (2111)  10
    #   upholstery (212)     200
    #   utilities (210)      70
    #  restaurants (200)     300

    # insert_ale_account(200, "expenses", None, 1)
    # insert_ale_account(210, "home", 200, 1)
    # insert_ale_account(211, "groceries", 210, 1)
    # insert_ale_account(2110, "supermarket", 211, 1)
    # insert_ale_account(2111, "farmers mkt", 211, 1)
    # insert_ale_account(212, "upholstery", 210, 1)
    # insert_ale_account(213, "utilities", 210, 1)
    # insert_ale_account(220, "restaurants", 200, 1)

    # insert_ale_account(300, "liabilities", None, -1)
    # insert_ale_account(400, "income", None, -1)
    # insert_ale_account(410, "salary", 400, -1)
    # insert_ale_account(411, "full time", 410, -1)
    # insert_ale_account(412, "odd jobs", 410, -1)
    
    # insert_ale_account(500, "equity", None, -1)

    # Use only one level of nesting
    insert_ale_account(100, "assets", None, 1)
    insert_ale_account(110, "checking", 100, 1)
    insert_ale_account(120, "savings", 100, 1)

    # purposely make parent ID greater than child's
    insert_ale_account(299, "expenses", None, 1)
    insert_ale_account(210, "groceries", 299, 1)
    insert_ale_account(220, "transportation", 299, 1)
    insert_ale_account(230, "restaurants", 299, 1)

    insert_ale_account(499, "income", None, -1)
    insert_ale_account(410, "full time", 499, -1)
    insert_ale_account(420, "odd jobs", 499, -1)

def create_ale_transaction():
    ex("""
    CREATE TABLE ale_transaction
    (id SMALLINT UNSIGNED,
    name VARCHAR(50),
    amount DECIMAL(12, 2),
    debit SMALLINT UNSIGNED,
    credit SMALLINT UNSIGNED,
    CONSTRAINT pk_tr_id PRIMARY KEY (id))""")

def insert_ale_transaction(id, name, amount, debit, credit):
    c = cnx.cursor()
    sql = """INSERT INTO ale_transaction (id, name, amount, debit, credit)
    VALUES (%s, %s, %s, %s, %s)"""
    
    c.execute(sql, (id, name, amount, debit, credit))
    cnx.commit()
    c.close()
    
def populate_ale_transaction():
    insert_ale_transaction(1, "feb salary", 3000.25, 110, 410)
    
    # added interactively
    # insert_ale_transaction(999, 'fix windshield', 90.12, 100, 420)

    insert_ale_transaction(2, "rice and beans", 30.10, 210, 110)
    insert_ale_transaction(3, "tomatoes", 5, 210, 110)
    insert_ale_transaction(4, "subway card", 90, 220, 110)
    insert_ale_transaction(5, "transfer", 500, 120, 110)
    insert_ale_transaction(6, "ramen", 15, 230, 110)
    insert_ale_transaction(7, "italian", 65, 230, 110)

def single_level_simple_debits():
    q("""
    SELECT a.id, a.name, sum(t_dr.amount) AS debits
    FROM ale_account AS a INNER JOIN ale_transaction AS t_dr
    ON t_dr.debit = a.id
    GROUP BY a.id, a.name""")

def single_level_simple_credits():
    q("""
    SELECT a.name, sum(t_cr.amount) AS credits
    FROM ale_account AS a INNER JOIN ale_transaction AS t_cr
    ON t_cr.credit = a.id
    GROUP BY a.name""")

def join_dr_cr():
    sql = """
    SELECT dr.id, dr.name, dr.parent, dr.debits, cr.credits FROM
    (SELECT a.id AS id, a.name AS name, a.parent AS parent, sum(t_dr.amount) AS debits
    FROM ale_account AS a
    LEFT JOIN ale_transaction AS t_dr
    ON t_dr.debit = a.id
    GROUP BY id, name) AS dr
    
    INNER JOIN
    
    (SELECT a.id AS id, a.name AS name, sum(t_cr.amount) AS credits
    FROM ale_account AS a
    LEFT JOIN ale_transaction AS t_cr
    ON t_cr.credit = a.id
    GROUP BY id, name) AS cr
    ON cr.id = dr.id
    """
    
    q(sql)

def combine_dr():
    sql = """
    SELECT a.id AS id, a.name AS name, sum(t_dr.amount) AS debits
    FROM ale_account AS a
    LEFT JOIN ale_transaction AS t_dr
    ON t_dr.debit = a.id OR a.id IN (SELECT parent FROM ale_account WHERE ID = t_dr.debit)
    WHERE a.parent IS NULL
    GROUP BY id, name"""

    q(sql)
