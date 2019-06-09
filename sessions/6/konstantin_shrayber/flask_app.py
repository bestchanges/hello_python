import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

from flask_app_storage import read_items, write_items, update_items

app = Flask(__name__)
CORS(app)

def gen_id():
    return str(uuid.uuid4())

items = []

@app.route("/items", methods=('GET',))
@read_items(items)
def get_items():
    return jsonify(items)

@app.route("/items", methods=('POST',), endpoint='post_items')
@write_items(items)
def post_items():
    item = request.get_json()
    item['id'] = gen_id()
    items.append(item)
    return jsonify(item)

@app.route("/items/<item_id>", methods=('PUT',), endpoint='put_items')
@update_items(items)
def put_items(item_id):
    item = request.get_json()
    for i in range(0, len(items)):
        if items[i]['id'] == item_id:
            items[i] = item
            break
    return jsonify(item)

@app.route("/items/<item_id>", methods=('DELETE',), endpoint='delete_items')
@update_items(items)
def delete_items(item_id):
    item = request.get_json()
    for i in items:
        if i['id'] == item_id:
            items.remove(i)
            break
    return jsonify(item)

@app.route("/")
def root():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=5001)