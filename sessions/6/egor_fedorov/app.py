import uuid

from flask import Flask, jsonify, request, redirect

app = Flask(__name__)


def gen_id():
    return str(uuid.uuid4())


items = [
    {
        'title': 'First',
        'id': gen_id(),
        'completed': False,
    },
    {
        'title': 'Second',
        'id': gen_id(),
        'completed': True,
    }
]


@app.route("/items", methods=('GET',))
def get_items():
    return jsonify(items)


@app.route("/items", methods=('POST',))
def post_items():
    item = request.get_json()
    item['id'] = gen_id()
    items.append(item)
    return jsonify(item)


@app.route("/items/<item_id>", methods=('PUT',))
def put_items(item_id):
    item = request.get_json()
    # TODO: search and update
    return jsonify(item)


@app.route("/")
def root():
    return redirect("/static/index.html")


if __name__ == '__main__':
    app.run(port=5001)
