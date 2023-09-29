from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET requests here
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Received a GET request!')

    def do_POST(self):
        # Handle POST requests here
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # Process the received data as per your requirements
        # For example, you can print it
        print(post_data.decode('utf-8'))
        # Send a response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Received the data successfully!')

host = "localhost" 
#sometimes just the word local host doesn't work, try using your actual IP address
#future fix will be to retrive this information with simple command or built-in function python has.
port = 8000

httpd = HTTPServer((host, port), RequestHandler)

print(f'Starting the server on {host}:{port}...')
httpd.serve_forever()