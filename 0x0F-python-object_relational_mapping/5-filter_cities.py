#!/usr/bin/python3
"""
5-filter_cities.py
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
    argument = argv[4]
    db_port = 3306

    query = """SELECT cities.name FROM cities
    INNER JOIN states ON  cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC"""
    try:
        db = MySQLdb.connect(host=db_host, port=db_port,
                             user=db_user, passwd=db_password,
                             db=db_db, charset="utf8")
        cur = db.cursor()
        cur.execute(query, (argument,))
        cities = cur.fetchall()
        list_result = []
        for row in cities:
            list_result.append(row[0])
        print(", ".join(list_result))

        cur.close()
        db.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
