from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/api/v1/menu', methods=['GET'])
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


@app.route('/api/v1/categories', methods=['GET'])
def categories():
    return jsonify([
        'Entries',
        'Main Dish',
        'Beverages'
    ])
