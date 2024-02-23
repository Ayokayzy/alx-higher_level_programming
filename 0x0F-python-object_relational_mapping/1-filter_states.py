#!/usr/bin/python3
"""
1-filter_states.py
"""
from sys import argv
import MySQLdb


def main():
    """
    lists all states from the database hbtn_0e_0_usa
    SystemArgs:
        argv[1]: mysql username,
        argv[2]: mysql password and
        argv[3]: database name
    """
    db_host = "localhost"
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_port = 3306

    try:
        db = MySQLdb.connect(host=db_host, port=db_port,
                             user=db_user, passwd=db_password,
                             db=db_db, charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT id, name FROM states WHERE \
CONVERT(name USING Latin1) \
COLLATE Latin1_General_CS LIKE 'N%' ORDER BY id ASC")
        states = cur.fetchall()

        for row in states:
            print(row)

        cur.close()
        db.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
