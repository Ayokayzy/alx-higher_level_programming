#!/usr/bin/python3
"""
9-model_state_filter_a.py
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine, delete
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

        for state in session.query(State).filter(State.name.like('%a%')).all():
            session.delete(state)
        session.commit()
        session.close()
    except Exception:
        pass
