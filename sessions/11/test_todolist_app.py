import pytest


@pytest.fixture()
def app():
    from todolist import app
    return app


@pytest.fixture()
async def client(app, aiohttp_client):
    return await aiohttp_client(app)


async def test_get_items(client):
    resp = await client.get('/items')
    assert 200 == resp.status
    json = await resp.json()
    assert 'First' == json[0]['title']