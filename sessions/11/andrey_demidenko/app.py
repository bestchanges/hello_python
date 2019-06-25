from aiohttp import web
from jsonschema import validate
import json

routes = web.RouteTableDef()
routes.static('/resources', 'resources')

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


@routes.get('/')
async def root(request):
    raise web.HTTPFound('/resources/index.html')


@routes.get('/todos')
async def todos_all(request):
    return web.json_response(todos_list())


def todos_list():
    try:
        with open(TODOS_FILE, encoding="utf-8") as todos_file:
            todos = json.load(todos_file)
    except IOError:
        todos = []

    return todos


@routes.put('/todos')
@routes.post('/todos')
@routes.delete('/todos')
async def manage_todos(request):
    todos = todos_list()
    task = await request.json()
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

    return web.json_response(task)


def save_todos(todos: dict):
    with open(TODOS_FILE, 'w', encoding="utf-8") as todos_file:
        json.dump(todos, todos_file)


@routes.get('/test')
async def example(request):
    return web.Response(text='Test Hello World')


app = web.Application()
app.add_routes(routes)
if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=5000)



