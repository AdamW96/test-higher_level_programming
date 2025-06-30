#!/usr/bin/env python3
"""
Flask API implementation with CRUD operations.

This module demonstrates how to create a RESTful API using Flask
with endpoints for user management, including GET and POST operations.
"""
from flask import Flask, jsonify, request

# Create Flask application instance
app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route('/')
def home():
    """
    Root endpoint that returns a welcome message.

    Returns:
        str: Welcome message
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    Get all usernames stored in the API.

    Returns:
        JSON: List of all usernames
    """
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def get_status():
    """
    Get API status.

    Returns:
        str: Status message
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Get a specific user by username.

    Args:
        username (str): The username to look up

    Returns:
        JSON: User data or error message
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the API.

    Expected JSON payload:
        {
            "username": "string",
            "name": "string",
            "age": int,
            "city": "string"
        }

    Returns:
        JSON: Confirmation message with user data or error message
    """
    try:
        # Get JSON data from request
        user_data = request.get_json()

        # Check if JSON data is provided
        if not user_data:
            return jsonify({"error": "No JSON data provided"}), 400

        # Check if username is provided
        if 'username' not in user_data:
            return jsonify({"error": "Username is required"}), 400

        username = user_data['username']

        # Add user to the users dictionary
        users[username] = {
            "username": username,
            "name": user_data.get('name', ''),
            "age": user_data.get('age', 0),
            "city": user_data.get('city', '')
        }

        # Return success response with user data
        response = {
            "message": "User added",
            "user": users[username]
        }

        return jsonify(response), 201

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.

    Returns:
        JSON: Error message
    """
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.

    Returns:
        JSON: Error message
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
