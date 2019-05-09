
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, send, rooms, leave_room

import logging
from logging import debug, info, warning
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chat_secret_haha'
socketio = SocketIO(app, logger=True)


@socketio.on('connect')
def on_connect():
    debug(f"Connected client {request.sid}")
    send("Hello Welcome to Chat Server. please send any message to me")


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


@socketio.on('my_rooms')
def handle_my_rooms():
    debug('asks for my rooms')
    send(rooms())


@app.route("/")
def index():
    return """
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('my response', function(msg) {
        $('#log').append('<p>Received: ' + msg.data + '</p>');
    });
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
    $('form#broadcast').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
        return false;
    });
});
"""

if __name__ == '__main__':
    socketio.run(app, port=5002)