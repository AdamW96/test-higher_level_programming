#!/usr/bin/env python3
"""
Simple HTTP server implementation using the http.server module.

This module demonstrates how to create a basic web server that can handle
different endpoints and serve JSON data using Python's built-in http.server.
"""
import http.server
import socketserver
import json
from urllib.parse import urlparse


class APIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the simple API server.

    This class handles different HTTP methods and routes requests
    to appropriate endpoints with JSON responses.
    """

    def do_GET(self):
        """
        Handle GET requests for different endpoints.
        """
        # Parse the URL to get the path
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/':
            # Root endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif path == '/data':
            # Data endpoint - serve JSON data
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_json_response(data)

        elif path == '/status':
            # Status endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif path == '/info':
            # Info endpoint
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_json_response(info_data)

        else:
            # 404 for undefined endpoints - return plain text
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    def send_json_response(self, data):
        """
        Send a JSON response with proper headers.

        Args:
            data (dict): The data to send as JSON
        """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        json_data = json.dumps(data)
        self.wfile.write(json_data.encode('utf-8'))

    def log_message(self, format, *args):
        """
        Override to customize logging format or suppress logs.
        """
        # Suppress default logging for cleaner output
        pass


def run_server(port=8000):
    """
    Run the HTTP server on the specified port.

    Args:
        port (int): The port number to run the server on
    """
    try:
        with socketserver.TCPServer(("", port), APIHandler) as httpd:
            print(f"Server running on http://localhost:{port}")
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as e:
        print(f"Error starting server: {e}")


if __name__ == "__main__":
    run_server(8000)
