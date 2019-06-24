import logging
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, rooms, join_room, leave_room


logging.basicConfig(filename='chat.log', level=logging.DEBUG)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connection():
    emit('response', 'Connected')


@socketio.on('message')
def handle_message(message):
    emit('response', message['data'], broadcast=True)
    app.logger.info(f"Message: {message['data']}")


@socketio.on('join')
def join(room):
    join_room(room)
    emit('response', f"'{request.sid}' joined the room '{room}'")
    app.logger.info(f"Rooms: {rooms()}")


@socketio.on('leave')
def leave(room):
    leave_room(room)
    emit('response', f"'{request.sid}' left the room '{room}'")
    app.logger.info(f"Rooms: {rooms()}")


@socketio.on('room_message')
def send_room_message(message):
    emit('response', message['data'], room=message['room'])
    app.logger.info(f"Room message: {message['data']}")


@socketio.on('client_rooms')
def handle_rooms():
    emit('response', rooms())
    app.logger.info(f"Client rooms: {rooms()}")


if __name__ == '__main__':
    socketio.run(app)
