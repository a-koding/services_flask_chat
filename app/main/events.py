from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import time


@socketio.on('joined', namespace='/chat')
def joined(message):
    emit('emitted_val', 'hiya got this from server')
@socketio.on('connect')
def test_connect():
    print('Client Connected')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('text', namespace='/chat')
