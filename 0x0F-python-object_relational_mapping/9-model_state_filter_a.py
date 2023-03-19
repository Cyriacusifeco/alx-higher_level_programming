#!/usr/bin/python3
""" Lists all State objects from that contain letter 'a'
from the db hbtn_0e_6_usa
Usage: ./9-model_state_filter_a.py <mysql username>\
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
    states = session.query(State).order_by(
        State.id).filter(State.name.like('%a%'))

    for state in states:
        print("{}: {}".format(state.id, state.name))
