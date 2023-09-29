from http.server import BaseHTTPRequestHandler, HTTPServer

# Create a custom request handler by subclassing BaseHTTPRequestHandler
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            # Try to decode the data as UTF-8
            s = post_data.decode('utf-8')
            print(s)
        except UnicodeDecodeError:
            # If decoding as UTF-8 fails, assume the data is binary and save it directly
            print("receiving file (binary)")
            with open('try3.jpg', 'wb') as file:
                file.write(post_data)
            print("\nFile has been copied successfully\n")

# Define the server host and port
host = '0.0.0.0'
port = 8000

# Create an HTTP server with the defined request handler
httpd = HTTPServer((host, port), RequestHandler)

# Start the server
print(f'Starting the server on {host}:{port}...')
httpd.serve_forever()
