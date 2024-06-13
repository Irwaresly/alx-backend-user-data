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

    def hash_password(password: str) -> bytes:
        """Generate a salted hash of the input password.
        Args:
            password (str): The password to be hashed.
        Returns:
            bytes: The hashed password.
        """
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
