from storage import *
from uuid import uuid4
from flask import Flask
from flask import request
from flask import jsonify
from data_validation import validate_item


app = Flask(__name__, static_url_path='')


def gen_id():
    return str(uuid4())


@app.route("/api/items", methods=["GET"])
def get_items():
    items = open_items()
    response = jsonify(items)
    response.status_code = 200
    return response


@app.route("/api/items", methods=["POST"])
def add_item():
    item = request.get_json()
    item['id'] = gen_id()
    validate_item(item)
    add_to_items(item)
    response = jsonify(item)
    response.status_code = 201
    return response


@app.route("/api/items/<item_id>", methods=["PUT"])
def edit_item(item_id):
    item = request.get_json()
    validate_item(item)
    delete_from_items(item_id)
    add_to_items(item)
    response = jsonify(item)
    response.status_code = 202
    return response


@app.route("/api/items/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    delete_from_items(item_id)
    response = jsonify("Deleted")
    response.status_code = 204
    return response


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(port=5001)
