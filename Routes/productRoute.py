from app import app
from flask import request
from Models.productModel import ProductModel
from Schemas.productSchema import ProductSchema,product_schema,products_schema
from db import db
# from Controller.productController import ProductController

@app.route('/')
def Index():
    return "<h1>Hello</h1>"

# Create a Product
@app.route('/product', methods=['POST'])
# ProductController.add_product(request)
def add_product():
    print("Request",request)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = ProductModel(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get All Products
@app.route('/product', methods=['GET'])
# ProductController.get_products()
def get_products():
    print("Request",request)
    all_products = ProductModel.query.all()
    result = products_schema.dump(all_products)
    return products_schema.jsonify(result.data)

# Get Single Product
@app.route('/product/<id>', methods=['GET'])
# ProductController.get_product(id)
def get_product(id):
    print("Request",request)
    product = ProductModel.query.get(id)
    return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
# ProductController.update_product(request,id)
def update_product(id):
    print("Request",request)
    product = ProductModel.query.get(id)

    product.name = request.json['name']
    product.description = request.json['description']
    product.price = request.json['price']
    product.qty = request.json['qty']

    db.session.commit()

    return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
# ProductController.delete_product(id)
def delete_product(id):
    print("Request",request)
    product = ProductModel.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)
