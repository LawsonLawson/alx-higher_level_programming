#!/usr/bin/python3
'''
Create a new table with the class definition of State
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    '''
    __tablename__ = "states"
    id = Column(Integer(), autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
