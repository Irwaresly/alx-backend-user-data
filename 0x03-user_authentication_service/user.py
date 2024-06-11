#!/usr/bin/env python3

"""
This module contains the SQLAlchemy model for the users table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model for the users table.

    Attributes:
        id (int): The primary key of the user.
        email (str): The email of the user, non-nullable.
        hashed_password (str): The hashed password of the user, non-nullable.
        session_id (str): The session ID of the user, nullable.
        reset_token (str): The reset token for the user, nullable.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
