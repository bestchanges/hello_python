from functools import reduce

from flask import Flask, jsonify, request, abort, Response
from logging import log, debug
import logging
import uuid

logging.basicConfig(level=logging.DEBUG)
app = Flask('todolist')

todolists = {
    'sample': {
        'name': 'sample',
        'items': [
            {
                'id': '1',
                'title': 'First task',
                'completed': False,
            },
            {
                'id': '2',
                'title': 'Second task',
                'completed': True,
            }
        ]
    }
}

EMPTY_TODOITEM = { 'title': '', 'completed': False}

@app.route("/")
def hello():
    return jsonify({'lists': list(todolists.keys())})


@app.route("/api/todoitem/<todolist_id>", methods=('GET', 'POST'))
def todoitems_endpoint(todolist_id):
    if not todolist_id in todolists:
        abort(404)
    items = todolists[todolist_id]['items']
    if request.method == 'POST':
        item = request.get_json()
        item['id'] = next_id(items)
        items.append(item)
        return jsonify(item)
    return jsonify(items)


@app.route("/api/todoitem/<todolist_id>/<item_id>", methods=('GET', 'PUT', 'DELETE'))
def todoitem_endpoint(todolist_id, item_id):
    if not todolist_id in todolists:
        abort(404)
    items = todolists[todolist_id]['items']
    if request.method == 'DELETE':
        item_index = item_index_by_id(items, item_id)
        if item_index is not None:
            del items[item_index]
        return Response(status=204)
    elif request.method == 'PUT':
        item = request.get_json()
        item_index = item_index_by_id(items, item_id)
        if item_index is None:
            abort(404)
        items[item_index] = item
        return jsonify(item)
    elif request.method == 'GET':
        return jsonify(items)


def next_id(items):
    return str(uuid.uuid4())
    # return reduce(lambda a, x: x['id'] if x['id'] > a else a, items, 0) + 1


def item_index_by_id(items, item_id):
    found = [i for i, x in enumerate(items) if x['id'] == item_id]
    return found[0] if found else None


if __name__ == '__main__':
    app.run()
