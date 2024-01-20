import sqlite3
conn = sqlite3.Connection("database.db")

with open("Create_database.sql", "r") as f:
    sql = f.read()
    
conn.executescript(sql)
conn.commit()
conn.close()