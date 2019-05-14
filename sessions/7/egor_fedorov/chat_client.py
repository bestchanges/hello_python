from flask_socketio import SocketIOTestClient


class ChatUser():
    def __init__(self, name, socketio_client: SocketIOTestClient) -> None:
        self.name = name
        self.client = socketio_client
        self.room = None

    def enter_room(self, room):
        self.room = room
        self.client.emit('join', {'room':self.room, 'name': self.name})


    def leave_room(self, room=None):
        if not room:
            room = self.room
        self.client.emit('leave', {'room': room})


    def my_rooms(self):
        self.client.emit('my_rooms')

    def send(self, message, room=None):
        """
        by default send message to the last entered room
        :param message:
        :param room:
        :return:
        """
        room = room or self.room
        self.client.send({'message': message, 'room': room}, True)
