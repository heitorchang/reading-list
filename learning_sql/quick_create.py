def quick_create(table_name, col_list):
    """
    Given a list of column names and types, create a table.
    quick_create("student" "id int, name str, dob date")
    quick_create("lunchmenu", "id int, name str, price money")
    quick_create("purchase", "id int, student_id int, menu_item int")
    """
    types = { 'varchar': 'VARCHAR(80)',
              'str': 'VARCHAR(80)',
              'int': 'INTEGER',
              'money': 'DECIMAL(12,2)',
              'float': 'FLOAT(18,6)',
              'date': 'DATE'
    }

    columns = col_list.split(",")

    sql = "CREATE TABLE " + table_name + "(\n"
    
    # col_data = [column.split() for column in columns]
    # col_sql = [col_elem[0] + " " + types[col_elem[1]] for col_elem in col_data]
    # sql += ",\n".join(col_sql)

    add_comma = False
    for column in columns:
        if add_comma:
            sql += ",\n"
        col_name, col_type = column.split()
        
        sql += col_name + " " + types[col_type]
        add_comma = True
    sql += ");"
    
    cursor = cnx.cursor()
    # print(sql)
    cursor.execute(sql)
    cursor.close()

def desc(table_name):
    cursor = cnx.cursor(buffered=True, named_tuple=True)
    cursor.execute("DESC " + table_name)

    for row in cursor:
        print(row.Field)

def quick_insert(table_name, values):
    sql = "INSERT INTO " + table_name + " VALUES "
    sql += str(values)
    sql += ";"
    
    cursor = cnx.cursor()
    # print(sql)
    cursor.execute(sql)
    cnx.commit()
    cursor.close()

def quick_next_id(table_name):
    cursor = cnx.cursor(named_tuple=True)
    cursor.execute("SELECT MAX(id) + 1 AS next_id FROM " + table_name)
    for row in cursor:
        print(row.next_id)
    cursor.close()

def quick_select_all(table_name):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM " + table_name)
    for row in cursor:
        print(row)
    cursor.close()
