import mysql.connector
from connect import connect

cnx = connect()

cursor = cnx.cursor()

try:
    cursor.execute("""
    CREATE TABLE `employees` (
    `emp_no` int(11) NOT NULL AUTO_INCREMENT,
    `first_name` varchar(14) NOT NULL,
    PRIMARY KEY (`emp_no`)) ENGINE=InnoDB""")

except mysql.connector.Error as err:
    print(err)
    
