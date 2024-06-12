#!usr/bin/env python3
'''function that uses the bcrypt package to hash a password string.
'''
import bcrypt


def _hash_password(password) -> bytes:
    '''Generate a salted hash of the input password
    '''
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
