#!/usr/bin/python3
"""
Prints all City objects from the db hbtn_0e_14_usa
Usage: ./14-model_city_fetch_by_state.py <mysql username>\
                                         <mysql passwd>\
                                         <database name>

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State
from sys import argv

if __name__ == "__main__":
    # create database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]))

    # create a transaction session
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
