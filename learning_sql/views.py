# p. 249

def create_totals_vw():
    cursor = cnx.cursor()
    cursor.execute("""
    CREATE VIEW customer_totals_vw
    (cust_id,
    cust_type_cd,
    cust_name,
    num_accounts,
    tot_deposits
    )
    AS
    SELECT cst.cust_id, cst.cust_type_cd,
    CASE
    WHEN cst.cust_type_cd = 'B' THEN
    (SELECT bus.name FROM business AS bus WHERE bus.cust_id = cst.cust_id)
    ELSE
    (SELECT concat(ind.fname, ' ', ind.lname)
    FROM individual AS ind
    WHERE ind.cust_id = cst.cust_id)
    END AS cust_name,
    SUM(CASE WHEN act.status = 'ACTIVE' THEN 1 ELSE 0 END) AS tot_active_accounts,
    SUM(CASE WHEN act.status = 'ACTIVE' THEN act.avail_balance ELSE 0 END) AS tot_balance
    FROM customer AS cst INNER JOIN account AS act
    ON act.cust_id = cst.cust_id
    GROUP BY cst.cust_id, cst.cust_type_cd;""")
    
    cursor.close()

def create_totals_tbl():
    cursor = cnx.cursor()
    # NOTE: creating this table freezes data; new data will not be reflected
    cursor.execute("""
    CREATE TABLE customer_totals
    AS
    SELECT * FROM customer_totals_vw;""")
    cursor.close()
