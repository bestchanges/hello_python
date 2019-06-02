import pytest


@pytest.fixture()
def app():
    from backend import app
    return app


@pytest.fixture()
async def client(app, aiohttp_client):
    return await aiohttp_client(app)


async def test_get_todos(client):
    resp = await client.get('/todos')
    assert resp.status == 200
    json = await resp.json()
    assert json is not None


# Did not have time to write tests properly to all backend methods, it was not TDD :(