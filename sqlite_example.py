import sqlite3

conn = sqlite3.connect('customer.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE customers (
    fist_name DATATYPE,
    last_name DATATYPE,
    email DATATYPE, 
     """)