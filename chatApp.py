from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
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
    socketio.run(app, debug=True)
