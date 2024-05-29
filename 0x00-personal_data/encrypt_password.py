#!/usr/bin/env python3
import bcrypt

'''
   This function takes a password as input and returns a hashed password as a byte string.
'''
def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Return the hashed password as a byte string
    return hashed_password
