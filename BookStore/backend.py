import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

    
def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
        
        
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book") # notice the absence of the conn.commit() statement for a select query
    rows = cur.fetchall()
    conn.close()
    return rows
    

def search(title="",author="",year="",isbn=""): # user may enter all 4 arguments or only 1 - to remove any errors,default values of empty strings are passed to the arguments
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn)) # notice the absence of the conn.commit() statement for a search query
    rows = cur.fetchall()
    conn.close()
    return rows
        

def delete(id):  # notice the argument is id
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))  # we did (id,) because a tuple is expected
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):  # notice the arguments - user may update all or one of the 4 attributes
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))  # notice the arguments
    conn.commit()
    conn.close()


# connect() will be executed as soon as import backend in frontend
connect()
#insert("The Monkey's Paw","Jacob",1977,94668413)
#delete(2)
#update(3,"The Monkey's Paw","W.J.Jacobs",1977,94668414)
#print(view())
#print(search(author="Jacob"))