from flask import Flask, jsonify, request, abort
from logging import log, debug
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask('todolist')

todolists = {
    'sample': {
        'name': 'sample',
        'items': {
            1: {
                'text': 'First task',
                'checked': False,
            },
            2: {
                'text': 'Second task',
                'checked': True,
            }
        }
    }
}

EMPTY_TODOLIST = { 'name': '', 'items': []}
EMPTY_TODOITEM = { 'text': '', 'checked': False}

@app.route("/")
def hello():
    return jsonify({'lists': list(todolists.keys())})


@app.route("/api/todolist", methods=('GET', 'POST'))
def todolists_endpoint():
    if request.method == 'POST':
        todolist = request.get_json()
        id = todolist['name']
        todolists[id] = {**EMPTY_TODOLIST, **todolist}
        return id
    return jsonify(list(todolists.keys()))


@app.route("/api/todolist/<todolist_id>", methods=('GET', 'POST', 'DELETE'))
def todolist_endpoint(todolist_id):
    if not todolist_id in todolists:
        abort(404)
    todolist = todolists[todolist_id]
    if request.method == 'DELETE':
        del todolists[todolist_id]
        return "OK"
    elif request.method == 'POST':
        item = {**EMPTY_TODOLIST, **request.get_json() }
        todolist[todolist_id] = item
        return str(todolist_id)
    else:
        return jsonify(todolist)


@app.route("/api/todoitem/<todolist_id>", methods=('GET', 'POST'))
def todoitems_endpoint(todolist_id):
    if not todolist_id in todolists:
        abort(404)
    items = todolists[todolist_id]['items']
    if request.method == 'POST':
        item = {**EMPTY_TODOITEM, **request.get_json()}
        item_id = max(items.keys()) + 1
        items[item_id] = item
        return jsonify(item_id)
    return jsonify(items)


@app.route("/api/todoitem/<todolist_id>/<int:item_id>", methods=('GET', 'POST', 'DELETE'))
def todoitem_endpoint(todolist_id, item_id):
    if not todolist_id in todolists:
        abort(404)
    items = todolists[todolist_id]['items']
    if request.method == 'DELETE':
        if not item_id in items:
            abort(404)
        del items[item_id]
        return "OK"
    elif request.method == 'POST':
        item = {**EMPTY_TODOITEM, **request.get_json()}
        items[item_id] = item
    return jsonify(items.get(item_id))


if __name__ == '__main__':
    app.run()
