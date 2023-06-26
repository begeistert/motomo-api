"""from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
"""

from flask import Flask, jsonify

app = Flask(__name__)
root = '/api/v1'


@app.route(f'{root}/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route(f'{root}/menu', methods=['GET'])
def menu():
    return jsonify({
        'Entries': {
            1: {
                'Name': 'Sopa Misa',
                'Description': 'Nuestra mejor sopa'
            },
            2: {
                'Name': 'Sushi de camarón',
                'Description': 'Nuestro mejor sushi'
            },
            3: {
                'Name': 'Pulpo asado',
                'Description': 'Nuevo platillo'
            },
            4: {
                'Name': 'Yakimeshi',
                'Description': 'Con verduras'
            }
        },
        'Main Dish':{
            11: {
                'Name': 'Ramen de cerdo ahumado',
                'Description': 'Sabroso y ahumado'
            },
            12: {
                'Name': 'Ramen vegano picante',
                'Description': 'Especiado y reconfortante'
            },
            13: {
                'Name': 'Ramen de pollo teriyaki',
                'Description': 'Dulce y satisfactorio'
            },
            14: {
                'Name': 'Ramen de mariscos',
                'Description': 'Delicioso y abundante'
            }
        },
        'Beverages': {
            21: {
                'Name': 'Café expresso',
                'Description': 'Intenso y aromático'
            },
            22: {
                'Name': 'Limonada refrescante',
                'Description': 'Cítrica y revitalizante'
            },
            23: {
                'Name': 'Agua de fresa',
                'Description': 'Dulce y cremoso'
            },
            24: {
                'Name': 'Té verde frío',
                'Description': 'Refrescante y saludable'
            }
        }
    })


@app.route(f'{root}/categories', methods=['GET'])
def categories():
    return jsonify([
        'Entries',
        'Main Dish',
        'Beverages'
    ])


if __name__ == '__main__':
    app.run()
