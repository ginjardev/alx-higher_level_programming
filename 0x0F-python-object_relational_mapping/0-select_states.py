#!/usr/bin/python3
""" 
Write a script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    conn = MySQLdb.connect(
        port = 3306,
        host='localhost',
        user=username,
        passwd=password,
        db=db_name
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()


if __name__ == '__main__':
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
