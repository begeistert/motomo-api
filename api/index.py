from flask import Flask, jsonify

app = Flask(__name__)

data = {
    'Entries': [
        {
            'id': 1,
            'name': 'Sopa Misa',
            'description': 'Nuestra mejor sopa',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 2,
            'name': 'Sushi de camarón',
            'description': 'Nuestro mejor sushi',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 3,
            'name': 'Pulpo asado',
            'description': 'Nuevo platillo',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 4,
            'name': 'Yakimeshi',
            'description': 'Con verduras',
            'price': '',
            'idImage': 0,
        }
    ],
    'Main Dish': [
        {
            'id': 11,
            'name': 'Ramen de cerdo ahumado',
            'description': 'Sabroso y ahumado',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 12,
            'name': 'Ramen vegano picante',
            'description': 'Especiado y reconfortante',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 13,
            'name': 'Ramen de pollo teriyaki',
            'description': 'Dulce y satisfactorio',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 14,
            'name': 'Ramen de mariscos',
            'description': 'Delicioso y abundante',
            'price': '',
            'idImage': 0,
        }
    ],
    'Beverages': [
        {
            'id': 21,
            'name': 'Café expresso',
            'description': 'Intenso y aromático',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 23,
            'Name': 'Limonada refrescante',
            'Description': 'Cítrica y revitalizante',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 24,
            'Name': 'Agua de fresa',
            'Description': 'Dulce y cremoso',
            'price': '',
            'idImage': 0,
        },
        {
            'id': 25,
            'Name': 'Té verde frío',
            'Description': 'Refrescante y saludable',
            'price': '',
            'idImage': 0,
        }
    ]
}


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/api/v1/menu', methods=['GET'])
def menu():
    return jsonify(data)


@app.route('/api/v1/menu/<category>', methods=['GET'])
def menu_category(category):
    return data[category]


@app.route('/api/v1/categories', methods=['GET'])
def categories():
    return jsonify(list(data.keys()))
