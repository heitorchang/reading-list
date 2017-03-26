def case_example():
    # Searched Case Expression
    sql = """
SELECT c.cust_id, c.fed_id,
  CASE
    WHEN c.cust_type_cd = 'I'
      THEN CONCAT(i.fname, ' ', i.lname)
    WHEN c.cust_type_cd = 'B'
      THEN b.name
    ELSE 'unknown'
  END AS name
FROM customer c LEFT OUTER JOIN individual i
  ON c.cust_id = i.cust_id
  LEFT OUTER JOIN business AS b
  ON c.cust_id = b.cust_id;
"""
    q(sql)

def subquery_in_then():
    q("""
    SELECT c.cust_id, c.fed_id,
    CASE
    WHEN c.cust_type_cd IN ('I', 'ind')
    THEN (SELECT CONCAT(i.fname, ' ', i.lname)
    FROM individual AS i WHERE i.cust_id = c.cust_id)
    WHEN c.cust_type_cd = 'B'
    THEN (SELECT b.name FROM business AS b
    WHERE b.cust_id = c.cust_id)
    ELSE 'Unknown'
    END AS name
    FROM customer AS c""")

def simple_case_expressions():
    """CASE VAR
    WHEN V1 THEN E1
    WHEN V2 THEN E2
    WHEN V3 THEN E3
    [ ELSE ED ]
    END

    can only check for equality between VAR and V0, V1, V2...
    """

    q("""SELECT customer.cust_id,
    CASE customer.cust_type_cd
    WHEN 'I' THEN
    (SELECT i.fname FROM individual AS i
    WHERE i.cust_id = customer.cust_id)
    WHEN 'B' THEN
    (SELECT b.name FROM business AS b
    WHERE b.cust_id = customer.cust_id)
    ELSE 'Unknown'
    END AS name
    FROM customer""")

def selective_aggregation():
    # p. 209-210
    q("""SELECT CONCAT('Alert: Account ', a.account_id, ' has incorrect balance') AS alert
    FROM account AS a
    WHERE (a.avail_balance, a.pending_balance) <>
    (SELECT
    SUM(CASE
    WHEN t.funds_avail_date > CURRENT_TIMESTAMP()
    THEN 0
    WHEN t.txn_type_cd = 'DBT'
    THEN t.amount * -1
    ELSE t.amount
    END),
    SUM(CASE
    WHEN t.txn_type_cd = 'DBT'
    THEN t.amount * -1
    ELSE t.amount
    END)
    FROM transaction t
    WHERE t.account_id = a.account_id);""")

def sum_txns():
    q("""SELECT account_id,
    SUM(CASE
    WHEN t.txn_type_cd = 'DBT'
    THEN t.amount * -1
    ELSE t.amount
    END) AS sum
    FROM transaction AS t
    GROUP BY account_id""")

def check_existence():
    q("""
    SELECT c.cust_id,
    CASE
    WHEN EXISTS (SELECT 1 FROM account a
    WHERE a.cust_id = c.cust_id
    AND a.product_cd = 'CHK') THEN 'Y'
    ELSE 'N'
    END AS has_checking
    FROM customer AS c""")
    
