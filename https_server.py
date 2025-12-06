# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import http.server
import ssl
import os

# Server configuration
HOST = "localhost"
PORT = 443
CERT_FILE = "/etc/ssl/private/localhost.crt"
KEY_FILE = "/etc/ssl/private/localhost.key"
DIRECTORY = "."  # Serve files from the current directory


# 'Access-Control-Max-Age': 6000,
# 'Access-Control-Allow-Origin': '*'
class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Max-Age', '6000')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        super().end_headers()

# Set up the HTTP server
# 'Access-Control-Allow-Origin' header
handler = CORSHandler
# also https://stackoverflow.com/questions/29954037/why-is-an-options-request-sent-and-can-i-disable-it
# Access-Control-Max-Age header can be up to 600
httpd = http.server.HTTPServer((HOST, PORT), handler)

# Wrap the socket with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

# Change to the directory to serve files from
os.chdir(DIRECTORY)
print(f"Serving HTTPS on https://{HOST}:{PORT} from {os.getcwd()}")
httpd.serve_forever()