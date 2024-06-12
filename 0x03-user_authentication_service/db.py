#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = scoped_session(sessionmaker(bind=self._engine))

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database

        Args:
            email (str): The email of the user
            hashed_password (str): The hashed password of the user

        Returns:
            User: The created User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        try:
            self.__session.add(new_user)
            self.__session.commit()
            self.__session.refresh(new_user)  # Refresh the instance
        except Exception as e:
            self.__session.rollback()
            new_user = None
            print(f"Error: {e}")
        finally:
            self.__session.remove()
        return new_user
