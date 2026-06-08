# program_10_crud_rest_api_project.py

from flask import Flask, jsonify, request

app = Flask(__name__)

products = []

# CREATE
@app.route("/products", methods=["POST"])
def create_product():

    product = request.get_json()

    products.append(product)

    return jsonify({
        "message":"Product Added"
    })

# READ
@app.route("/products", methods=["GET"])
def get_products():

    return jsonify(products)

# UPDATE
@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):

    for product in products:

        if product["id"] == id:

            product["name"] = request.json["name"]
            product["price"] = request.json["price"]

            return jsonify({
                "message":"Updated",
                "data":product
            })

    return jsonify({
        "message":"Product Not Found"
    })

# DELETE
@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):

    global products

    products = [
        p for p in products
        if p["id"] != id
    ]

    return jsonify({
        "message":"Deleted"
    })

if __name__ == "__main__":
    app.run(debug=True)