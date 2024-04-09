#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections! """

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM states\
        INNER JOIN cities ON states.id = cities.state_id\
        WHERE states.name LIKE %s\
        ORDER BY cities.id ASC;",
        (sys.argv[4],),
    )
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
