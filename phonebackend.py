import sqlite3

def create():
    con=sqlite3.connect('phone.db')
    curs=con.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS phones(id INTEGER PRIMARY KEY, name text, num integer)')
    con.commit()
    con.close()

def viewing():
    con=sqlite3.connect('phone.db')
    curs=con.cursor()
    curs.execute('SELECT * FROM phones')
    numb=curs.fetchall()
    con.close()
    return numb
def update(name,num):
    con=sqlite3.connect('phone.db')
    curs=con.cursor()
    curs.execute('UPDATE phones SET name=?,num=? WHERE id=?',('name,num'))
    con.commit()
    con.close()

def deleting(id):
    con=sqlite3.connect('phone.db')
    curs=con.cursor()
    curs.execute('DELETE FROM phones WHERE id=?',(id,))
    con.commit()
    con.close()

def insert(name,num):
    con = sqlite3.connect('phone.db')
    curs = con.cursor()
    curs.execute('INSERT INTO phones VALUES(NULL,?,?)', (name,num))
    con.commit()
    con.close()

def search(name='',num=''):
    conn=sqlite3.connect('phone.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM phones WHERE name=? OR num=?')
    rows=cur.fetchall()
    conn.close()
    return rows

create()