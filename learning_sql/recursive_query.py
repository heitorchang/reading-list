# http://stackoverflow.com/questions/16513418/how-to-do-the-recursive-select-query-in-mysql

def populate_recursive_table():
    ex("""
    CREATE TABLE item_parent
    (item INT,
    parent INT)""")

    cursor = cnx.cursor()
    sql = """
    INSERT INTO item_parent (item, parent)
    VALUES (%s, %s);"""

    cursor.execute(sql, (1, None))
    cursor.execute(sql, (2, 1))
    cursor.execute(sql, (3, 1))
    cursor.execute(sql, (4, 2))
    cursor.execute(sql, (5, 4))
    cursor.execute(sql, (6, 3))
    
def select_recursive(item_id):
    sql = """
    SELECT t.item AS item_id, @parent := t.parent as parent
    FROM (SELECT * from item_parent ORDER BY item DESC) AS t
    CROSS JOIN (SELECT @parent := %s) AS tmp
    WHERE t.item = @parent;"""

    c = cnx.cursor()
    c.execute(sql, (item_id,))
    
    for row in c:
        print(row)
    c.close()
