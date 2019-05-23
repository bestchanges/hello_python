from flask import Flask, request, jsonify, redirect
from jsonschema import validate
import json

app = Flask(__name__, static_folder='resources')
TODOS_FILE = 'todos.json'


TODO_SCHEMA = {
     "type": "object",
     "properties": {
         "id": {"type": "number"},
         "title": {"type": "string"},
         "completed": {"type": "boolean"},
     },
    "required": ["id", "title", "completed"]
}

@app.route("/")
def root():
    return redirect('/resources/index.html')


@app.route("/todos", methods=['GET'])
def todos_all():
    return jsonify(todos_list())


def todos_list():
    try:
        with open(TODOS_FILE, encoding="utf-8") as todos_file:
            todos = json.load(todos_file)
    except IOError:
        todos = []

    return todos


@app.route("/todos", methods=['PUT', 'POST', 'DELETE'])
def manage_todos():
    todos = todos_list()
    task = request.get_json()
    validate(instance=task, schema=TODO_SCHEMA)
    if task['id'] == 0:
        max_id = max([todo['id'] for todo in todos]) if len(todos) > 0 else 0
        task['id'] = max_id + 1

    if request.method == 'PUT':
        todos.append(task)

    if request.method == 'POST':
        for index, todo in enumerate(todos):
            if todo['id'] == task['id']:
                todos[index] = task

    if request.method == 'DELETE':
        for index, todo in enumerate(todos):
            if todo['id'] == task['id']:
                del todos[index]

    save_todos(todos)

    return jsonify(task)


def save_todos(todos: dict):
    with open(TODOS_FILE, 'w', encoding="utf-8") as todos_file:
        json.dump(todos, todos_file)


if __name__ == '__main__':
    app.run(port=5000)



