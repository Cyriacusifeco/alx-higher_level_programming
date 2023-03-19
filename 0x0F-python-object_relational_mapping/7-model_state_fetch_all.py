#!/usr/bin/python3
""" Lists all State objects from the db hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all.py <mysql username>\
                                    <mysql passwd>\
                                    <database name>
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
    result = session.query(State).order_by(State.id)

    for state in result:
        print("{}: {}".format(state.id, state.name))
