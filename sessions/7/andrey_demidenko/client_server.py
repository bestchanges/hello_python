from flask import Flask, render_template, session, request, redirect, make_response, jsonify
from flask_socketio import SocketIO, emit
from hashlib import md5
from time import time, strftime, gmtime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
users = []
messages = []


@app.route('/')
def chat_page():
    if 'user_id' in session:
        return render_template('index.html', users=users, user_id=session['user_id'], messages=messages)
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        session['user_id'] = md5(str(time()).encode('utf-8')).hexdigest()
        session['user_name'] = request.form['username']
        return redirect('/')
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    for index, user in enumerate(users):
        if user['user_id'] == session['user_id']:
            del users[index]
    resp = make_response(jsonify({'status': 'ok'}))
    resp.delete_cookie('session')
    return resp


@app.before_request
def before_request():
    if 'user_id' in session and len(session['user_id']):
        user_id = session['user_id']
        user_name = session['user_name']
        if user_id not in [user['user_id'] for user in users]:
            users.append({'user_id': user_id, 'user_name': user_name})


@socketio.on('message')
def handle_message(message):
    message = {'message': message, 'user_id': session['user_id'], 'username': session['user_name'], 'time': strftime("%H:%M:%S", gmtime(time()))}
    messages.append(message)
    emit('message', message, broadcast=True)


@socketio.on('user_connected')
def handle_connected():
    emit('refresh_users', users, broadcast=True)


@socketio.on('user_logout')
def handle_logout():
    emit('refresh_users', users, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
