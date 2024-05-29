#!/usr/bin/env python3
"""A module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def validate_password(password: str, hashed_password: bytes) -> bool:
    """Validates a password against a hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

