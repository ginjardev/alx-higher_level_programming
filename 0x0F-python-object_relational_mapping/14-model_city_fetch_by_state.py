#!/usr/bin/python3
""" prints all City objects from
the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state_cities = session.query(City, State).join(
        State)
    for city, state in state_cities.all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
