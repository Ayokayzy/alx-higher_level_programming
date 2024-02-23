#!/usr/bin/python3
"""
100-relationship_states_cities.py
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from relationship_city import City
from relationship_state import State, Base


if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    try:
        engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost:3306/{}"
                .format(username, passwd, db_name),
                pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        nstate = State(name="California")
        city = City(name="San Francisco", state=nstate)

        session.add(city)
        session.commit()

        session.close()
    except Exception:
        pass
