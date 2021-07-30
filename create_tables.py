import sqlite3

con = sqlite3.connect('testdb.db')

cursor = con.cursor()

create_table_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
create_table_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)"

# To run the query
cursor.execute(create_table_users)
cursor.execute(create_table_items)

con.commit()
con.close()
