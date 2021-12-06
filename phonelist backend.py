import sqlite3

def create():
    con=sqlite3.connect('phone.db')
    curs=con.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS book(name TEXT, phone_number INTEGER)')
    con.commit()
    con.close()

