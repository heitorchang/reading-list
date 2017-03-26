import sys
import mysql.connector
import os

# IMPORTANT: cnx.commit() must be called after INSERT, UPDATE, and DELETE
# Also, if external changes are made (such as in PHPMyAdmin), cnx.commit()
# must be called for these changes to be seen.

if os.name == 'posix':
    sys.path.insert(0, '/home/heitor/reading-list/learning_sql/')
    from config_ubuntu import config

    db_config = config
else:
    sys.path.insert(0, 'C:/Users/Heitor/Desktop/emacs-24.3/bin/reading-list/learning_sql/')
    from config_ptl import config

def connect():
    return mysql.connector.connect(**config)

def simple_query(cnx, sql):
    cursor = cnx.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    
    return rows

def print_simple_query(cnx, sql):
    cursor = cnx.cursor(named_tuple=True)
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()

    # print()  # add a newline
    for row in rows:
        print(row)

def global_cnx(sql):
    # assumes a cnx = connect() command has been executed
    print_simple_query(cnx, sql)

def q(sql):
    global_cnx(sql)
    
def ex(sql):
    cursor = cnx.cursor()
    cursor.execute(sql)
    cnx.commit()
    cursor.close()

cnx = connect()
print("cnx is your connection.")
