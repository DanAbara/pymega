# I installed postgresql from command line. NO default password for default 'postgres' user.
# Use 'sudo su postgres' to switch to postgres user and then run psql. Authentication is by default 'ident' meaning you must be connected as default OS user which is 'postgres'

# its easier to get postgreSQL and pgadmin set up on unix by adding the official PGDG repository:

#$ curl -s https://salsa.debian.org/postgresql/postgresql-common/raw/master/pgdg/apt.postgresql.org.sh | sudo bash

#$ sudo apt-get update

#$ sudo apt-get install postgresql-10 pgadmin4

#// or

#$ sudo apt-get install postgresql pgadmin4


import psycopg2 # small scale portable dbase

def create_table():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='ubuntu123' host='127.0.0.1' port='5432' ") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("CREATE TABLE if NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") # REAL is a float. IF NOT EXISTS checks if the table exists already
    conn.commit() # save changes
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='ubuntu123' host='127.0.0.1' port='5432' ") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("CREATE TABLE if NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price)) -- prone to sql injection
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit() # save changes
    conn.close()

def view():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='ubuntu123' host='127.0.0.1' port='5432' ") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='ubuntu123' host='127.0.0.1' port='5432' ") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='ubuntu123' host='127.0.0.1' port='5432' ") # create a connection
    cur=conn.cursor() # create a cursor object
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

# insert("Water Glass",10,5)
# insert("Tea cup",150,11.05)
# delete("Tea cup")
# update(11,10.6,"Apple")

print(view()) # view the selected rows

#create_table()