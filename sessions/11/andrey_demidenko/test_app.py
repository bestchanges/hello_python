from app import app


async def test_hello(aiohttp_client, loop):
    client = await aiohttp_client(app)
    resp = await client.get('/test')
    assert resp.status == 200
    text = await resp.text()
    assert 'Test Hello World' in text