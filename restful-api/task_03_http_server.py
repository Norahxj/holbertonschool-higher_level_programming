#!/usr/bin/python3
"""
Task 03: Develop a simple API using http.server
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Handles HTTP GET requests for the simple API
    """

    def do_GET(self):
        """
        Handle GET requests and route endpoints
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    """
    Starts the HTTP server on port 8000
    """
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
