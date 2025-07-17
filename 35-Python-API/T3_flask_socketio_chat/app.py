from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
socketio = SocketIO(app)

@app.route('/')
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    # Use eventlet for production-like async
    socketio.run(app, host='0.0.0.0', port=5000)
