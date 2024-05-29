import bcrypt

salt = bcrypt.gensalt()
print(salt)  # Example output: b'$2b$12$KIXkPpBjKALtEEeYpYhixe'

