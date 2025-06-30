#!/usr/bin/env python3
"""
Flask API with authentication and authorization.

This module demonstrates various authentication methods including
Basic Auth and JWT tokens, along with role-based access control.
"""
from flask import Flask, jsonify, request, HTTPBasicAuth, JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

# Create Flask application instance
app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-string'  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  # For testing purposes

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic Authentication
@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials for basic authentication.

    Args:
        username (str): The username
        password (str): The password

    Returns:
        str or None: Username if credentials are valid, None otherwise
    """
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh token required errors."""
    return jsonify({"error": "Fresh token required"}), 401


# Routes
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Route protected with basic authentication.

    Returns:
        str: Success message
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint that returns a JWT token.

    Expected JSON payload:
        {
            "username": "string",
            "password": "string"
        }

    Returns:
        JSON: Access token or error message
    """
    try:
        # Get credentials from request
        credentials = request.get_json()

        if not credentials:
            return jsonify({"error": "No credentials provided"}), 401

        username = credentials.get('username')
        password = credentials.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password required"}), 401

        # Verify credentials
        if username in users and check_password_hash(users[username]['password'], password):
            # Create JWT token with user info
            additional_claims = {"role": users[username]["role"]}
            access_token = create_access_token(
                identity=username,
                additional_claims=additional_claims
            )
            return jsonify({"access_token": access_token})
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"error": "Server error"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Route protected with JWT authentication.

    Returns:
        str: Success message
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Route that requires admin role.

    Returns:
        str: Success message or error
    """
    # Get current user from JWT token
    current_user = get_jwt_identity()
    claims = get_jwt()

    # Check if user has admin role
    if claims.get('role') == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403


@app.errorhandler(401)
def handle_unauthorized(e):
    """Handle unauthorized access."""
    return jsonify({"error": "Unauthorized access"}), 401


@app.errorhandler(403)
def handle_forbidden(e):
    """Handle forbidden access."""
    return jsonify({"error": "Forbidden access"}), 403


if __name__ == '__main__':
    app.run(debug=True)
