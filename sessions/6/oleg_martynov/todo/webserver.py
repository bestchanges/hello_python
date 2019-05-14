from flask import Flask, request, jsonify, make_response, Response
import os
import json
import uuid

DEFAULT_DATAFILE = "todos.json"

todos = []


def load_data(path=DEFAULT_DATAFILE):
    if os.path.exists(path):
        with open(path) as todos_file:
            todos = json.load(todos_file)


def save_data(path=DEFAULT_DATAFILE):
    with open(path, "w+") as todos_file:
        json.dump(todos, todos_file)


app = Flask(__name__, static_url_path="")

@app.route("/api")
def api():
    return Response(status=200)


@app.route("/api/todos", methods=["GET"])
def return_todos():
    if request.method == "GET":
        print("GET")
        app.logger.debug("got GET")
        return jsonify(todos)

@app.route("/api/todos", methods=["POST"])
def create_todo():
    global todos
    backup_todos = todos[:]
    if request.method == "POST":
        try:
            app.logger.debug("got POST: {}".format(request.get_json()))
            new_todo = request.get_json()
            new_todo_id = str(uuid.uuid4())
            new_todo["id"] = new_todo_id
            app.logger.debug("adding new todo record: {}".format(json.dumps(new_todo)))
            todos.append(new_todo)
            save_data()
            return make_response(jsonify({"id": new_todo_id}), 200)
        except Exception as e:
            app.log_exception(e)
            todos = backup_todos
            return Response(status=500)


@app.route("/api/todos/<todo_id>", methods=["PUT", "DELETE"])
def manage_todos(todo_id):
    global todos
    backup_todos = todos[:]
    try:
        if request.method == "PUT":
            app.logger.debug("got PUT: {}".format(request.get_json()))
            updated_todo = request.get_json()
            for i in range(len(todos)):
                if todos[i]["id"] == todo_id:
                    app.logger.debug("old todo: {}, new todo: {}".format(todos[i], updated_todo))
                    todos[i] = updated_todo
            save_data()
            return Response(status=200)
        elif request.method == "DELETE":
            app.logger.debug("got DELETE: {}".format(request.get_json()))
            for i in range(len(todos)):
                if todos[i]["id"] == todo_id:
                    app.logger.debug("deleting todo: {}".format(todos[i]))
                    del todos[i]
                    break
            save_data()
            return Response(status=200)
    except Exception as e:
        app.log_exception(e)
        todos = backup_todos
        return Response(status=500)

load_data()
app.run(port=5001, debug=True)
