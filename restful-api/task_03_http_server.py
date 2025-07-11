#!/usr/bin/env python3
"""
Simple HTTP server implementation using the http.server module.
"""
import http.server
import socketserver
import json
from urllib.parse import urlparse

class APIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the simple API server.
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
        """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        json_data = json.dumps(data)
        self.wfile.write(json_data.encode('utf-8'))


def run_server(port=8000):
    """
    Run the HTTP server on the specified port.
    """
    try:
        with socketserver.TCPServer(("", port), APIHandler) as httpd:
            print(f"Server running on http://localhost:{port}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as e:
        print(f"OS Error: {e}")


if __name__ == "__main__":
    run_server(8000)
