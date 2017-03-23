import sys
import mysql.connector
import os

if os.name == 'posix':
    sys.path.insert(0, '/home/heitor/reading-list/learning_sql/')
    from config_ubuntu import config

    db_config = config
else:
    sys.path.insert(0, 'C:/Users/Heitor/Desktop/emacs-24.3/bin/reading-list/learning_sql/')
    from config_ptl import config

def connect():
    return mysql.connector.connect(**config)
