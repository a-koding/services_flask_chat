#!/bin/env python
from app import create_app, socketio
from flask_cors import CORS

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app,port=3000)
