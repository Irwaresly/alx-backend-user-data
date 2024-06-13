#!/usr/bin/env python3
"""A module for authentication-related routines.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Generate a salted hash of the input password.
    Args:
        password (str): The password to be hashed.
    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
