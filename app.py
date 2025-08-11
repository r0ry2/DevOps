from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello")  

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Running server on port 8000...")
    httpd.serve_forever()
