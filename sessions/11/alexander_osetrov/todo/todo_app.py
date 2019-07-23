from items import Item
from uuid import uuid4
from aiohttp import web
from queries import DBQuery
from jsonschema import validate
from jsonschema.exceptions import ValidationError


routes = web.RouteTableDef()

schema = {
     "type": "object",
     "properties": {
         "completed": {"type": "boolean"},
         "id": {"type": "string"},
         "order": {"type": "number"},
         "title": {"type": "string"}
     }
}


@routes.get('/')
async def index(request):
    return web.HTTPFound('/index.html')


@routes.get('/api/items')
async def get_items(request):
    with DBQuery() as db:
        items = db.get_items()
    return web.json_response(items)


@routes.post('/api/items')
async def add_item(request):
    item = await request.json()
    item['id'] = str(uuid4())
    try:
        validate(instance=item, schema=schema)
        with DBQuery() as db:
            values = Item(**item)
            db.add_item(values)
        return web.json_response(item, status=201)
    except ValidationError as e:
        response = {'error': e.message}
        return web.json_response(response, status=400)


@routes.put('/api/items/{item_id}')
async def edit_item(request):
    item = await request.json()
    item_id = request.match_info['item_id']
    try:
        validate(instance=item, schema=schema)
        with DBQuery() as db:
            db.update_item(item_id, item)
        return web.json_response(item, status=202)
    except ValidationError as e:
        response = {'error': e.message}
        return web.json_response(response, status=400)


@routes.delete('/api/items/{item_id}')
async def delete_item(request):
    item_id = request.match_info['item_id']
    with DBQuery() as db:
        db.delete_item(item_id)
    return web.Response(status=204)


app = web.Application()
app.add_routes(routes)
app.router.add_route('GET', '/', index)
app.router.add_static('/', './static')


if __name__ == "__main__":
    web.run_app(app, host='localhost', port=5001)
