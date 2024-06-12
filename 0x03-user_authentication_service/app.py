#!/usr/bin/env python3
"""
Basic Flask app with a single GET route ("/") returning a JSON payload.

This script sets up a Flask app with a GET route that returns a JSON response.

Routes:
    GET '/' - Returns a JSON payload: {"message": "Bienvenue"}
"""

from flask import Flask, jsonify

# Create the Flask application
app = Flask(__name__)


# Define a route for the root endpoint
@app.route('/')
def index() -> str:
    """Route handler for the root endpoint.

    Returns:
        dict: JSON payload with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
