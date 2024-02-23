#!/usr/bin/python3
"""
10-model_state_my_get.py
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    argument = argv[4]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, db_name))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).\
            filter(State.name == argument).first()
        if state:
            print("{}".format(state.id))
        else:
            print("Not found")
        session.close()
    except Exception:
        pass
