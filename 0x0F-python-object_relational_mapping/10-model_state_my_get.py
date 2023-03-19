#!/usr/bin/python3
""" Prints the State obj with the name passed as argument
from the db hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql username>\
                                    <mysql passwd>\
                                    <database name>\
                                    <state name to search>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    found = 0
    for state in session.query(State):
        if state.name == argv[4]:
            print("{}".format(state.id))
            found = 1
            break
    if found == 0:
        print("Not found")
