import socketio
import logging

logging.basicConfig(level=logging.DEBUG)
sio = socketio.Client()


def reader():
    print("Hello this is SocketIO chat client")
    while True:
        try:
            message = input("Say: ")
            if message == "exit":
                break
            sio.send(message)
            #sio.emit('json', {'message': message})
        except:
            break
    sio.disconnect()


@sio.on('connect')
def on_connect():
    print('connection established')

@sio.on('message')
def on_message(data):

    print(data)

@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')

sio.start_background_task(reader)
sio.connect('http://localhost:5002', transports=['websocket'])
sio.wait()