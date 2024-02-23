#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


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

        query_rows = session.query(State, City).\
            join(City).order_by(City.id).all()
        for state, city in query_rows:
            print('{}: ({}) {}'.format(state.name, city.id, city.name))
        session.close()
    except Exception:
        pass
