from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

data = {
    'Entries': [
        {
            'id': 1,
            'name': 'Sopa Misa',
            'dsc': 'Nuestra mejor sopa',
            'price': 95.0,
            'img': 0,
        },
        {
            'id': 2,
            'name': 'Sushi de camarón',
            'dsc': 'Nuestro mejor sushi',
            'price': 85.0,
            'img': 0,
        },
        {
            'id': 3,
            'name': 'Pulpo asado',
            'dsc': 'Nuevo platillo',
            'price': 90.0,
            'img': 0,
        },
        {
            'id': 4,
            'name': 'Yakimeshi',
            'dsc': 'Con verduras',
            'price': 110.0,
            'img': 0,
        }
    ],
    'Main': [
        {
            'id': 11,
            'name': 'Ramen de cerdo ahumado',
            'dsc': 'Sabroso y ahumado',
            'price': 95.0,
            'img': 0,
        },
        {
            'id': 12,
            'name': 'Ramen vegano picante',
            'dsc': 'Especiado y reconfortante',
            'price': 85.0,
            'img': 0,
        },
        {
            'id': 13,
            'name': 'Ramen de pollo teriyaki',
            'dsc': 'Dulce y satisfactorio',
            'price': 90.0,
            'img': 0,
        },
        {
            'id': 14,
            'name': 'Ramen de mariscos',
            'dsc': 'Delicioso y abundante',
            'price': 110.0,
            'img': 0,
        }
    ],
    'Beverages': [
        {
            'id': 21,
            'name': 'Café expresso',
            'dsc': 'Intenso y aromático',
            'price': 50.0,
            'img': 0,
        },
        {
            'id': 23,
            'Name': 'Limonada refrescante',
            'dsc': 'Cítrica y revitalizante',
            'price': 60.0,
            'img': 0,
        },
        {
            'id': 24,
            'Name': 'Agua de fresa',
            'dsc': 'Dulce y cremoso',
            'price': 90.0,
            'img': 0,
        },
        {
            'id': 25,
            'Name': 'Té verde frío',
            'dsc': 'Refrescante y saludable',
            'price': 55.0,
            'img': 0,
        }
    ]
}

orders = {}


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


@app.route('/api/v1/orders', methods=['GET', 'POST'])
def order():
    global orders

    if request.method == 'POST':
        _order = request.get_json()
        _uuid = str(uuid.uuid4())
        _order['uuid'] = _uuid
        orders[_uuid] = _order
        return jsonify(_order)
    else:
        _uuid = request.args.get('uuid')
        if _uuid is None:
            return jsonify(list(orders.values()))
        else:
            return jsonify(orders[_uuid])


if __name__ == '__main__':
    app.run(debug=True)