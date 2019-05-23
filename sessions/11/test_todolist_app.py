from aiohttp import web

from todolist import app


async def test_hello(aiohttp_client, loop):
    client = await aiohttp_client(app)
    resp = await client.get('/items')
    assert resp.status == 200
    json = await resp.json()
    assert 'First' == json[0]['title']