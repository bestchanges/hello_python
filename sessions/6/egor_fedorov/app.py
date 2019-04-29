from flask import Flask, jsonify, request, abort

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
        item = {**EMPTY_TODOITEM, **request.get_json() }
        id = max(todolist.keys()) + 1
        todolist[id] = item
        return str(id)
    else:
        return jsonify(todolist)


@app.route("/api/todoitem/<list>/<int:item_id>", methods=('GET', 'POST', 'DELETE'))
def todoitem_endpoint(list, item_id):
    list_ = todolists[list]
    if request.method == 'DELETE':
        if not item_id in list_:
            abort(404)
        del list_[item_id]
        return "OK"
    elif request.method == 'POST':
        item = request.get_json()
        list_[item_id] = item
    return jsonify(list_.get(item_id))


if __name__ == '__main__':
    app.run()
