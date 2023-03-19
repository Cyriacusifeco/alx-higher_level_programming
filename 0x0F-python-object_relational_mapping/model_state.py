#!/usr/bin/python3
""" A python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Model class that inherits from Base

    __tablename__: The name of mysql table to store states
    id: The id of state
    name: The state name
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
