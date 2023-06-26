"""from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
"""

from microdot import Microdot

app = Microdot()


@app.route('/')
def index(request):
    return 'Hello World!'


if __name__ == '__main__':
    app.run()