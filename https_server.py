import http.server
import ssl
import logging
import sys
import signal

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set content type to JavaScript and allow cross-origin requests
        self.send_header('Content-Type', 'application/javascript')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow cross-origin requests
        super().end_headers()

# Set up logging for better output visibility
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create an SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
try:
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
except ssl.SSLError as e:
    logging.error(f"Error loading SSL certificate and key: {e}")
    sys.exit(1)

# Create the HTTP server
server_address = ('0.0.0.0', 8080)
httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)

# Wrap the server socket with SSL
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

# Gracefully handle shutdown (Ctrl+C)
def handle_shutdown(signal, frame):
    logging.info("\nServer is shutting down...")
    httpd.server_close()
    logging.info("Server stopped gracefully.")
    sys.exit(0)

# Handle Ctrl+C (SIGINT) to stop the server
signal.signal(signal.SIGINT, handle_shutdown)

# Start the server
logging.info(f"Serving HTTPS on {server_address[0]}:{server_address[1]} with SSL encryption.")
try:
    httpd.serve_forever()
except Exception as e:
    logging.error(f"Server encountered an error: {e}")
    httpd.server_close()
    sys.exit(1)
