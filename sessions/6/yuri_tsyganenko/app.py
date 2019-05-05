from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)




def gen_id():
    return str(uuid.uuid4())


@app.route("/items")
def root():
    return "Hello, root"


items = [
    {"title": "One1",
     "id": gen_id(),
     'completed': True
     },
    {"title": "Two2",
     "id": gen_id(),
     'completed': False
     },
]


if __name__ == '__main__':
    app.run(port=5001)


@app.route("/items")
def items():
    print(" NOW- /ITEMS *****************")
    return jsonify(items)


@app.route("/items", methods=('GET',))
def get_items():
    print(" GET_method /ITEMS *****************")
    return jsonify(items)


@app.route("/items", methods=('POST',))
def post_items():
    print("POST_method /ITEMS *****************")
    item = request.get_json()
    item['id'] = gen_id()
    items.append(item)
    return jsonify(items)


def find_item(id):
    for item in items:
        if item["id"] == id:
            return item
    raise ValueError("No item found with id: " + id)


@app.route("/items/<item_id>", methods=('PUT',))        #  WHY POST is shown in console ???
def update_item(item_id):
    print("PUT_method  ***************** " + item_id)
    items.remove(find_item(item_id))
    new_values_item = request.get_json()
    items.append(new_values_item)
    return jsonify(items)
