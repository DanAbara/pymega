import sqlite3 # small scale portable dbase

def create_table():
    conn=sqlite3.connect("lite.db") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("CREATE TABLE if NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") # REAL is a float. IF NOT EXISTS checks if the table exists already
    conn.commit() # save changes
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("CREATE TABLE if NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit() # save changes
    conn.close()

def view():
    conn=sqlite3.connect("lite.db") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

# insert("Water Glass",10,5)
# insert("Coffee cup",10,5)
# delete("Water Glass")
# update(11,10.6,"Coffee cup")

print(view()) # view the selected rows
