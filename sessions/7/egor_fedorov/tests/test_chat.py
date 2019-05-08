import logging

import pytest
from flask_socketio import SocketIOTestClient
from pytest import fail

from chat_client import ChatUser

@pytest.fixture
def app():
    from chat_server import app
    return app


@pytest.fixture
def socketio():
    from chat_server import socketio
    return socketio

@pytest.fixture
def user(app, socketio) -> ChatUser:
    return ChatUser('Ivan', socketio.test_client(app))


@pytest.fixture(scope='function')
def user2(app, socketio) -> ChatUser:
    return ChatUser('Sonia', socketio.test_client(app))


def test_connect(user: ChatUser):
    assert user.client.is_connected()


def test_join_room(user: ChatUser, user2: ChatUser):
    user.enter_room('hello_python')
    msg = f"{user.name} has entered the room."
    assert in_recieved(msg, user.client.get_received())
    assert not in_recieved(msg, user2.client.get_received())
    user2.enter_room('hello_python')
    msg = f"{user2.name} has entered the room."
    assert in_recieved(msg, user.client.get_received())
    assert in_recieved(msg, user2.client.get_received())


def test_send_to_room(user: ChatUser, user2: ChatUser):
    room = 'hello_python'
    user.enter_room(room)
    user2.enter_room(room)
    msg = f"Hello from {user.name}"
    user.send(msg, room=room)
    assert in_recieved(msg, user.client.get_received())
    assert in_recieved(msg, user2.client.get_received())



def in_recieved(message, received):
    for item in received:
        if item['name'] == 'message' and message in item['args']:
            return True
    return False


def test_send_ping(user: ChatUser, user2: ChatUser):
    msg = "Hello to me only"
    user.send(msg)
    assert user is not user2
    assert user.client.sid != user2.client.sid
    assert in_recieved(msg, user.client.get_received())
    assert not in_recieved(msg, user2.client.get_received())


def test_my_rooms(user: ChatUser):
    assert user.client.get_received() == []
    user.my_rooms()
    assert len(user.client.get_received().pop()['args']) == 1
    user.enter_room("some")
    user.my_rooms()
    assert len(user.client.get_received().pop()['args']) == 2
