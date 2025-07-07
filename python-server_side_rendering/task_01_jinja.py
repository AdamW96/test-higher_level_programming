#!/usr/bin/env python3
"""
Flask Application with Jinja Templates
File: task_01_jinja.py

This Flask application demonstrates:
- Basic Flask setup and routing
- Jinja2 template rendering
- Reusable template components
- Multiple page navigation
"""

from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)


# ============================================================================
# Routes
# ============================================================================

@app.route('/')
def home():
    """
    Home page route
    Renders the main index.html template
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    About page route
    Renders the about.html template
    """
    return render_template('about.html')


@app.route('/contact')
def contact():
    """
    Contact page route
    Renders the contact.html template
    """
    return render_template('contact.html')


# ============================================================================
# Application startup
# ============================================================================

if __name__ == '__main__':
    # Run Flask application in debug mode on port 5000
    app.run(debug=True, port=5000)
