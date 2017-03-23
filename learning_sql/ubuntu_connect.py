import sys
import mysql.connector
import os

if os.name == 'posix':
    sys.path.insert(0, '/home/heitor/reading-list/learning_sql/')
    from config_ubuntu import config

    db_config = config
else:
    pass

def connect() {
    cnx = mysql.connector.connect(**config)
}
