#!/usr/bin/env python3
"""A module for authentication-related routines.
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    @staticmethod
    def hash_password(password: str) -> bytes:
        """Generate a salted hash of the input password.
        Args:
            password (str): The password to be hashed.
        Returns:
            bytes: The hashed password.
        """
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Parameters:
        email (str): User's email.
        password (str): User's password.

        Returns:
        User: The new User object if successful.

        Raises:
        ValueError: If a user with the same email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_password = Auth.hash_password(password)
            new_user = self._db.add_user(
                    email=email, hashed_password=hashed_password
            )
            return new_user
