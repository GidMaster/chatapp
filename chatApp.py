from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('./ChatAppPage.html')

@socketio.on('connection')
def handleEvent(json):
    print(f'recived: {str(json)}')
    socketio.emit('logResponse', json)

@socketio.on('sendMessage')
def handleEvent(json):
    print(f'recived: {str(json)}')
    socketio.emit('messageResponse', json)

if __name__ == '__main__':
    socketio.run(app, port=int("80"), debug=True)
