import sqlite3

try:
    conexion_user = sqlite3.connect("database/database_user.sqlite3", check_same_thread=False)
    
except Exception as ex:
    print(ex)