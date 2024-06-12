#!/usr/bin/env python3
"""
Basic Flask app with a single GET route ("/") returning a JSON payload.

This script sets up a Flask app with a GET route that returns a JSON response.

Routes:
    GET '/' - Returns a JSON payload: {"message": "Bienvenue"}
"""

from flask import Flask, jsonify
from flask import request
from auth import Auth

# Create an instance of the Auth class
AUTH = Auth()

# Create the Flask application
app = Flask(__name__)


# Define a route for the root endpoint
@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Route handler for the root endpoint.

    Returns:
        dict: JSON payload with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """Route handler for the /users endpoint.

    Returns:
    dict: JSON payload with the registration status.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
