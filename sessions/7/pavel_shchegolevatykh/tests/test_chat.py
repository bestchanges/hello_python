import pytest
from flask_socketio import SocketIOTestClient


@pytest.fixture(scope='function')
def app():
    from chat_server import app
    return app


@pytest.fixture(scope='function')
def socketio():
    from chat_server import socketio
    return socketio


@pytest.fixture(scope='function')
def client1(socketio, app):
    return socketio.test_client(app)


@pytest.fixture(scope='function')
def client2(socketio, app):
    return socketio.test_client(app)


def in_received(message, received):
    for item in received:
        if item['name'] == 'message' and message in item['args']:
            return True
    return False


def test_connect_client1(client1: SocketIOTestClient):
    assert client1.is_connected()


def test_connect_client2(client2: SocketIOTestClient):
    assert client2.is_connected()


def test_welcome_received(client1: SocketIOTestClient, client2: SocketIOTestClient):
    assert client1.sid != client2.sid
    assert client2.get_received() == [{
        'name': 'message',
        'args': 'Welcome to our chat. Now you can send messages',
        'namespace': '/'
    }]


def test_join_room(client1: SocketIOTestClient, client2: SocketIOTestClient):
    room = 'test_room'
    client1_name = 'Bill'
    client1.emit('join', {'room': room, 'name': client1_name})
    msg = f"{client1_name} has entered the room."
    assert in_received(msg, client1.get_received())
    assert not in_received(msg, client2.get_received())
    client2_name = 'Gill'
    client2.emit('join', {'room': room, 'name': client2_name})
    msg = f"{client2_name} has entered the room."
    assert in_received(msg, client1.get_received())
    assert in_received(msg, client2.get_received())


def test_send_to_room(client1: SocketIOTestClient, client2: SocketIOTestClient):
    room = 'test_room'
    client1_name = 'Bill'
    client2_name = 'Gill'
    client1.emit('join', {'room': room, 'name': client1_name})
    client2.emit('join', {'room': room, 'name': client2_name})
    msg = f"Hello from {client1_name}"
    client1.send({'message': msg, 'room': room}, True)
    assert in_received(msg, client1.get_received())
    assert in_received(msg, client2.get_received())

