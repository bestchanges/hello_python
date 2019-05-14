import pytest
from flask_socketio import SocketIOTestClient


@pytest.fixture
def app():
    from chat import app
    return app


@pytest.fixture
def server():
    from chat import socketio
    return socketio


@pytest.fixture
def client(server, app):
    return server.test_client(app)


@pytest.fixture
def client2(server, app):
    return server.test_client(app)


def test_connect(client: SocketIOTestClient):
    assert client.is_connected()


def test_chat(client: SocketIOTestClient, client2: SocketIOTestClient):
    assert client.sid != client2.sid
    client.send("Hello chat!")
    assert client2.get_received() == [{'name': 'Hello chat!', 'args': [None], 'namespace': '/'}]

