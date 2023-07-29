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
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968271-9499c990-087a-4194-a29e-8de47104e01a.jpg'
        },
        {
            'id': 2,
            'name': 'Sushi de camarón',
            'dsc': 'Nuestro mejor sushi',
            'price': 85.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968386-691f8463-0b26-4009-acb1-3176945888ab.jpeg'
        },
        {
            'id': 3,
            'name': 'Pulpo asado',
            'dsc': 'Nuevo platillo',
            'price': 90.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968426-93e012de-593c-4b69-8859-7859a8687f1b.jpeg'
        },
        {
            'id': 4,
            'name': 'Yakimeshi',
            'dsc': 'Con verduras',
            'price': 110.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968453-7495bd2e-79ba-48b7-b4f2-bff9ce0fb1d2.jpeg'
        }
    ],
    'Main': [
        {
            'id': 11,
            'name': 'Ramen de cerdo ahumado',
            'dsc': 'Sabroso y ahumado',
            'price': 95.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968503-97b22881-ce57-4f54-a2d2-fae016abf440.jpg'
        },
        {
            'id': 12,
            'name': 'Ramen vegano picante',
            'dsc': 'Especiado y reconfortante',
            'price': 85.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968531-8598e7a0-ceef-4b76-845c-02019735e877.jpg'
        },
        {
            'id': 13,
            'name': 'Ramen de pollo teriyaki',
            'dsc': 'Dulce y satisfactorio',
            'price': 90.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968546-9918aea4-9ba8-4a0d-a758-930cd23c9c75.jpg'
        },
        {
            'id': 14,
            'name': 'Ramen de mariscos',
            'dsc': 'Delicioso y abundante',
            'price': 110.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968559-8b669d90-baeb-4bd0-9968-ff6306daaf29.jpg'
        }
    ],
    'Beverages': [
        {
            'id': 21,
            'name': 'Café expresso',
            'dsc': 'Intenso y aromático',
            'price': 50.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968578-fe67cbfb-7dd7-4d74-b476-96d329ff75f4.jpeg'
        },
        {
            'id': 23,
            'Name': 'Limonada refrescante',
            'dsc': 'Cítrica y revitalizante',
            'price': 60.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968596-17769368-77db-490e-9ff0-c904654c5949.jpeg'
        },
        {
            'id': 24,
            'Name': 'Agua de fresa',
            'dsc': 'Dulce y cremoso',
            'price': 90.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968607-d1903316-c19f-426b-a38f-82b6b0539089.jpg'
        },
        {
            'id': 25,
            'Name': 'Té verde frío',
            'dsc': 'Refrescante y saludable',
            'price': 55.0,
            'img': 0,
            'url': 'https://github-production-user-asset-6210df.s3.amazonaws.com/36460223/256968618-f9fc18ce-fd9d-476f-b29f-c7a6baf2128e.jpeg'
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