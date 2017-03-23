def add_employee(cnx, emp_name):
    sql = """INSERT INTO employees
    (first_name)
    VALUES (%s)"""

    cursor.execute(sql, (emp_name,))

    emp_no = cursor.lastrowid
    
    cnx.commit()
    return emp_no
