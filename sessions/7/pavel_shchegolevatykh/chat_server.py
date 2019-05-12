from flask import Flask, request
from flask_socketio import SocketIO, join_room, send, leave_room
from logging import debug

import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_chat_secret'
socketio = SocketIO(app)


@socketio.on('connect')
def on_connect():
    debug(f"Connected client {request.sid}")
    send("Welcome to our chat. Now you can send messages")


@socketio.on('join')
def on_join(data):
    username = data['name']
    room = data['room']
    debug(f"Client {request.sid} with username {username} joined {room}")
    join_room(room)
    send(username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    room = data['room']
    debug(f"Client {request.sid} leaves {room}")
    leave_room(room)
    send(f'You has leaved room {room} ')


@socketio.on('message')
def on_message(message):
    send(f'{request.sid}: {message} ', broadcast=True)


@socketio.on('json')
def handle_json(data):
    debug('received message: ' + str(data))
    if 'message' in data:
        room = data.get('room')
        send(data['message'], room=room)


if __name__ == '__main__':
    socketio.run(app, port=5002)
