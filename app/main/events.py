from flask import session,request
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import time
import jwt
active_c_users={}

@socketio.on('joined', namespace='/chat')
def joined(data):
    #here we are creating a new room
    #active_c_users[data['jwt_token']]=request.sid
    #decoded = jwt.decode(data['jwt_token'], verify=False)
    room = 'ashok_friend'
    join_room(room)
    print('Room created Successfully')

@socketio.on('u_s', namespace='/chat')
def get_msg(message):
    room = 'ashok_friend'
    emit('s_u', message, room=room,include_self=False)

@socketio.on('send_typing', namespace='/chat')
def send_typing(typing):
    room = 'ashok_friend'
    emit('receive_typing', typing, room=room,include_self=False)

@socketio.on('leave')
def on_leave(data):
    del active_c_users[request.sid]
    leave_room(request.sid)

@socketio.on('connect')
def test_connect():
    print('Client Connected')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')