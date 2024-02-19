#!/usr/bin/python3
"""
11-model_state_insert.py
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, db_name))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        foundstate = session.query(State).filter(State.id == 2).first()
        foundstate.name = 'New Mexico'
        session.commit()
        session.close()
    except Exception:
        pass
