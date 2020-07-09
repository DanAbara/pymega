import sqlite3

class Database:

    def __init__(self): # __init__ is the standard constructor to declare classes and is the function that is run when the class is called.
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    # func Add entry
    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    # func View all
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    # func search entry - with different options. Default empty values means function will run even though not all values are passed when called.
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    # func delete
    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    # func update
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self): # to delete the instance when the script is exited.
        self.conn.close()
        
#connect()
#insert("West African verse","Gladys May",1940,29485943)
#delete(2)
#update(4,"New West African verse","Gladys May Casey Hayford",1941,445345)
#print(view())
#print(search(author="Lehnard Jeung"))
