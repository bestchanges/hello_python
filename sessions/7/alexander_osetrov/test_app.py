import pytest
from flask_socketio import SocketIOTestClient


@pytest.fixture
def app():
    from chat_server import app
    return app


@pytest.fixture
def server():
    from chat_server import socketio
    return socketio


@pytest.fixture
def client(server, app):
    return server.test_client(app)


@pytest.fixture
def client_2(server, app):
    return server.test_client(app)


def test_connection(client: SocketIOTestClient):
    assert client.is_connected()
    received = client.get_received()
    assert received[0]['args'][0] == "Connected"


def test_message(client: SocketIOTestClient, client_2: SocketIOTestClient):
    assert client.sid != client_2.sid
    client.emit('message', {"data": "Test Message"})
    received_message = client_2.get_received()[1]['args'][0]
    assert received_message == "Test Message"


def test_room_joining(client: SocketIOTestClient):
    client.emit('join', 'Test Room')
    join_message = client.get_received()[1]['args'][0]
    assert join_message == f"'{client.sid}' joined the room 'Test Room'"
    client.emit('client_rooms')
    rooms = client.get_received()[0]['args'][0]
    assert rooms == [client.sid, 'Test Room']


def test_room_leaving(client: SocketIOTestClient):
    client.emit('join', 'Test Room')
    join_message = client.get_received()[1]['args'][0]
    assert join_message == f"'{client.sid}' joined the room 'Test Room'"
    client.emit('client_rooms')
    room_joined = client.get_received()[0]['args'][0]
    assert sorted(room_joined) == sorted([client.sid, 'Test Room'])
    client.emit('leave', 'Test Room')
    leave_message = client.get_received()[0]['args'][0]
    assert leave_message == f"'{client.sid}' left the room 'Test Room'"
    client.emit('client_rooms')
    room_left = client.get_received()[0]['args'][0]
    assert room_left == [client.sid]


def test_room_message(client: SocketIOTestClient):
    client.emit('join', 'Test Room')
    join_message = client.get_received()[1]['args'][0]
    assert join_message == f"'{client.sid}' joined the room 'Test Room'"
    client.emit('client_rooms')
    room_joined = client.get_received()[0]['args'][0]
    assert sorted(room_joined) == sorted([client.sid, 'Test Room'])
    client.emit('room_message', {'data': "Test room message", 'room': "Test Room"})
    room_message = client.get_received()[0]['args'][0]
    assert room_message == "Test room message"
