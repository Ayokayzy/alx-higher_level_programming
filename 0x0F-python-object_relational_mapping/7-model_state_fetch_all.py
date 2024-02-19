#!/usr/bin/python3
"""
7-model_state_fetch_all.py
"""
from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for id, name in session.query(State.id, State.name):
        print("{}: {}".format(id, name))
