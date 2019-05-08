import uuid
from flask import Flask, jsonify, request, redirect
app = Flask(__name__, static_folder="todo")


items = dict()


@app.route("/")
def index():
    return redirect("/todo/index.html")


@app.route("/items", methods=("GET", ))
def get_items():
    return jsonify(list(items.values()))


@app.route("/items", methods=("POST", ))
def add_item():
    item = request.get_json()
    item_id = uuid.uuid4().hex
    item['id'] = item_id
    items[item_id] = item
    return jsonify(item)


@app.route("/items/<item_id>", methods=("PUT", ))
def update_item(item_id):
    new_item = request.get_json()
    items[item_id]['title'] = new_item['title']
    items[item_id]['completed'] = new_item['completed']
    return jsonify(new_item)


@app.route("/items/<item_id>", methods=("DELETE", ))
def delete_item(item_id):
    del items[item_id]
    return ""


if __name__ == "__main__":
    app.run()
