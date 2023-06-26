"""from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
"""

from flask import Flask, Blueprint

bp = Blueprint('v1', __name__, template_folder='templates')

app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/api/v1')


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/v1/', methods=['GET'])
def categories():
    pass


if __name__ == '__main__':
    app.run()
