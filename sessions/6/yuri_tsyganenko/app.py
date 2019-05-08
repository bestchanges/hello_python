from flask import Flask, jsonify, request
from jsonschema import validate
import uuid

app = Flask(__name__)

schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "id": {"type": "string"},
        "completed": {"type": "boolean"},
    },
    "required": ["title", "id", "completed"]
}

def gen_id():
    return str(uuid.uuid4())



items_list = [
    {"title": "One1",
     "id": gen_id(),
     'completed': True
     },
    {"title": "Two2",
     "id": gen_id(),
     'completed': False
     },
]


@app.route("/items")
def items():
    print(" NOW- /ITEMS *****************")
    return jsonify(items_list)


@app.route("/items", methods=('GET',))
def get_items():
    print(" GET_method /ITEMS *****************")
    return jsonify(items_list)


@app.route("/items", methods=('POST',))
def post_items():
    print("POST_method /ITEMS *****************")
    item = request.get_json()
    print("type item" + str(type(item)))
    validate(item, schema)
    item['id'] = gen_id()
    items_list.append(item)
    return jsonify(items_list)


def find_item(id):
    for item in items_list:
        if item["id"] == id:
            return item
    raise ValueError("No item found with id: " + id)


@app.route("/items/<item_id>", methods=('PUT',))        #  WHY POST is shown in console ???
def update_item(item_id):
    print("PUT_method  ***************** " + item_id)
    items_list.remove(find_item(item_id))
    new_values_item = request.get_json()
    new_values_item["id"] = item_id
    validate(new_values_item, schema)
    items_list.append(new_values_item)
    return jsonify(items_list)

if __name__ == '__main__':
    app.run(port=5001)
