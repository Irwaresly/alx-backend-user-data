#!usr/bin/env python3
'''
This module contains the User class, which is the SQLAlchemy model for the
users table in the database. The User class inherits from the SQLAlchemy
Base class and defines
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    '''
    This class represents the users table in the database.
    '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
