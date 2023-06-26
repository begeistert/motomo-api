"""from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
"""

from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'


@app.route('/api', methods=['GET', 'POST'])
def index():
    return 'Hello world!'


app.run()
