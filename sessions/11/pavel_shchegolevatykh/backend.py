import uuid
import json
import aiofiles

from aiohttp import web
from jsonschema import validate

routes = web.RouteTableDef()
routes.static('/static', './static')

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


def gen_id():
    return str(uuid.uuid4())


todos = []


async def save_to_file():
    async with aiofiles.open('todos.json', mode='w') as file_handle:
        contents = json.dumps(todos)
        await file_handle.write(contents)


async def read_from_file():
    async with aiofiles.open('todos.json', mode='r') as file_handle:
        contents = await file_handle.read()
        return json.loads(contents)


@routes.get('/todos')
async def get_todos(request):
    global todos
    todos = await read_from_file()
    return web.json_response(todos)


@routes.post('/todos')
async def post_todos(request):
    todo = await request.json()
    validate(instance=todo, schema=insert_schema)
    todo['id'] = gen_id()
    todos.append(todo)
    await save_to_file()
    return web.json_response(todo)


@routes.put('/todos/{todo_id}')
async def put_items(request):
    todo_id = request.match_info['todo_id']
    todo = await request.json()
    validate(instance=todo, schema=update_schema)
    for t in todos:
        t.update(('completed', todo['completed']) for k, v in t.items() if k == 'id' and v == todo_id)
        t.update(('title', todo['title']) for k, v in t.items() if k == 'id' and v == todo_id)
    await save_to_file()
    return web.json_response(todo)


@routes.delete('/todos/{todo_id}')
async def delete_items(request):
    todo_id = request.match_info['todo_id']
    deleted_todo = next((todo for todo in todos if todo['id'] == todo_id))
    todos.remove(deleted_todo)
    await save_to_file()
    return web.json_response(deleted_todo)


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=5001)
