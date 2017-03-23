import os
import sys

# Ubuntu
if os.name == 'posix':
    sys.path.insert(0, '/home/heitor/reading-list/learning_sql/')
else:
    # Windows
    sys.path.insert(0, 'C:/Users/Heitor/Desktop/emacs-24.3/bin/reading-list/learning_sql/')
