#!/usr/bin/python

import sqlite3

con = sqlite3.connect('wf.db')

with con:

    cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS nodes;")
    # cur.execute("CREATE TABLE nodes(id INT, name TEXT, childrenIds text)")
    # cur.execute("INSERT INTO nodes VALUES(1,'n1', '2,3')")
    # cur.execute("INSERT INTO nodes VALUES(2,'n2','')")
    cur.execute("INSERT INTO nodes VALUES(5,'n5','')")


    
with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM nodes")
    # rows = cur.fetchmany(2)
    rows = cur.fetchall()

    print(rows)