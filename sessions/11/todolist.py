import uuid

from aiohttp import web

routes = web.RouteTableDef()


def gen_id():
    return str(uuid.uuid4())


default_items = [
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

session = {}

@routes.get("/items")
async def get_items(request):
    items = session.setdefault('items', default_items)
    return web.json_response(items)


@routes.post("/items")
async def post_items(request):
    items = session.setdefault('items', default_items)
    item = await request.get_json()
    item['id'] = gen_id()
    items.append(item)
    session.modified = True
    return web.json_response(item)


@routes.put("/items/<item_id>")
async def put_items(request):
    item = request.get_json()
    # TODO: search and update
    return web.json_response(item)


@routes.get("/")
async def root():
    raise web.HTTPFound("/static/index.html")

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)