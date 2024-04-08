#!/usr/bin/python3

import MySQLdb


def list_states(username, password, db_name):
	conn = MySQLdb.connect(host='localhost', user=username, password=password, db=db_name)
	cur = conn.cursor()
	cur.execute("SELECT * FROM states ORDER BY states.id ASC")
	states = cur.fetchall()
	for state in states:
		print(state)


if __name__ == '__main__':
    list_states("root", "password", "hbtn_0e_0_usa")
