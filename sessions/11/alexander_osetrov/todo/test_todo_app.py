import json
import pytest


@pytest.fixture
def app():
    from todo_app import app
    app._loop = None
    return app


@pytest.fixture
async def client(app, aiohttp_client):
    return await aiohttp_client(app)


@pytest.fixture
def todo_db():
    from queries import DBQuery
    with DBQuery() as db:
        yield db


async def test_index(client):
    response = await client.get('/')
    assert response.status == 200


async def test_get_items(client, todo_db):
    response = await client.get('/api/items')
    assert response.status == 200
    response_items = await response.json()
    storage_items = todo_db.get_items()
    assert response_items == storage_items


async def test_add_item(client, todo_db):
    new_item = {'title': "test_add_item", "completed": False, "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 201
    response_item = await response.json()
    assert response_item['title'] == new_item['title']
    assert response_item['completed'] == new_item['completed']
    todo_db.delete_item(response_item['id'])


async def test_save_item(client, todo_db):
    new_item = {'title': "test_save_item", "completed": False, "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 201
    response_item = await response.json()
    storage_items = todo_db.get_items()
    assert storage_items[-1]['title'] == new_item['title']
    assert storage_items[-1]['completed'] == new_item['completed']
    assert storage_items[-1]['id'] == response_item['id']
    todo_db.delete_item(response_item['id'])


async def test_edit_item(client, todo_db):
    new_item = {'title': "test_edit_item", "completed": False, "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 201
    response_item = await response.json()
    response_item['title'] = "edited_item"
    response_item['completed'] = True
    item_id = response_item['id']
    response = await client.put(f'/api/items/{item_id}', data=json.dumps(response_item))
    assert response.status == 202
    edited_item = await response.json()
    assert edited_item['id'] == response_item['id']
    assert edited_item['title'] == "edited_item"
    assert edited_item['completed'] is True
    todo_db.delete_item(item_id)


async def test_delete_item(client, todo_db):
    new_item = {'title': "test_delete_item", "completed": False, "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 201
    response_item = await response.json()
    item_id = response_item['id']
    delete = await client.delete(f'/api/items/{item_id}')
    assert delete.status == 204
    # assert delete.text == "Deleted"
    storage_items = todo_db.get_items()
    for item in storage_items:
        assert item['title'] != "test_delete_item"
        assert item['id'] != response_item['id']


async def test_post_invalid_order_type(client, todo_db):
    new_item = {'title': "test_post_invalid_order_type", "completed": False, "order": "4"}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 400
    response_item = await response.json()
    assert response_item == {'error': "'4' is not of type 'number'"}
    storage_items = todo_db.get_items()
    for item in storage_items:
        assert item['title'] != "test_invalid_order_type"


async def test_put_invalid_order_type(client, todo_db):
    new_item = {'title': "test_invalid_order_type", "completed": False, "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 201
    response_item = await response.json()
    item_id = response_item['id']
    new_item['order'] = "4"
    new_item['title'] = "test_put_invalid_order_type"
    edit_response = await client.put(f'/api/items/{item_id}', data=json.dumps(new_item))
    assert edit_response.status == 400
    response_msg = await edit_response.json()
    assert response_msg == {'error': "'4' is not of type 'number'"}
    storage_items = todo_db.get_items()
    for item in storage_items:
        assert item['title'] != "test_put_invalid_order_type"
    todo_db.delete_item(item_id)


async def test_validate_completed_type(client, todo_db):
    new_item = {'title': "test_invalid_completed_type", "completed": "Completed", "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 400
    response_item = await response.json()
    assert response_item == {'error': "'Completed' is not of type 'boolean'"}
    storage_items = todo_db.get_items()
    for item in storage_items:
        assert item['title'] != "test_invalid_completed_type"


async def test_put_invalid_completed_type(client, todo_db):
    new_item = {'title': "test_invalid_completed_type", "completed": False, "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 201
    response_item = await response.json()
    item_id = response_item['id']
    new_item['completed'] = "Completed"
    new_item['title'] = "test_put_invalid_completed_type"
    edit_response = await client.put(f'/api/items/{item_id}', data=json.dumps(new_item))
    assert edit_response.status == 400
    response_msg = await edit_response.json()
    assert response_msg == {'error': "'Completed' is not of type 'boolean'"}
    storage_items = todo_db.get_items()
    for item in storage_items:
        assert item['title'] != "test_put_invalid_completed_type"
    todo_db.delete_item(item_id)


async def test_validate_title_type(client, todo_db):
    new_item = {'title': 123, "completed": False, "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 400
    response_item = await response.json()
    assert response_item == {'error': f"123 is not of type 'string'"}
    storage_items = todo_db.get_items()
    for item in storage_items:
        assert item['title'] != 123


async def test_put_invalid_title_type(client, todo_db):
    new_item = {'title': "test_invalid_title_type", "completed": False, "order": 4}
    response = await client.post('/api/items', data=json.dumps(new_item))
    assert response.status == 201
    response_item = await response.json()
    item_id = response_item['id']
    new_item['title'] = 123
    edit_response = await client.put(f'/api/items/{item_id}', data=json.dumps(new_item))
    assert edit_response.status == 400
    response_msg = await edit_response.json()
    assert response_msg == {'error': "123 is not of type 'string'"}
    storage_items = todo_db.get_items()
    for item in storage_items:
        assert item['title'] != 123
    todo_db.delete_item(item_id)
