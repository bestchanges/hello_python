import uuid
import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from jsonschema import validate

update_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "id": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "required": ["title", "id", "completed"]
}

insert_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "id": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "required": ["title"]
}

app = Flask(__name__)
CORS(app)


def gen_id():
    return str(uuid.uuid4())


todos = []


def save_to_file():
    with open('todos.json', 'w') as file_handle:
        json.dump(todos, file_handle)


def read_from_file():
    with open('todos.json', 'r') as file_handle:
        todos = json.load(file_handle)


@app.route('/todos', methods=['GET'])
def get_todos():
    read_from_file()
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def post_todos():
    todo = request.get_json()
    validate(instance=todo, schema=insert_schema)
    todo['id'] = gen_id()
    todos.append(todo)
    save_to_file()
    return jsonify(todo)


@app.route("/todos/<todo_id>", methods=['PUT'])
def put_items(todo_id):
    todo = request.get_json()
    validate(instance=todo, schema=update_schema)
    for t in todos:
        t.update(('completed', todo['completed']) for k, v in t.items() if k == 'id' and v == todo_id)
    save_to_file()
    return jsonify(todo)


@app.route("/todos/<todo_id>", methods=['DELETE'])
def delete_items(todo_id):
    deleted_todo = next((todo for todo in todos if todo['id'] == todo_id))
    todos.remove(deleted_todo)
    save_to_file()
    return jsonify(deleted_todo)


if __name__ == '__main__':
    app.run(port=5001)
