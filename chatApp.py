from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return('Hello Wolrd!')

if __name__ == '__main__':
    socketio.run(app, debug=True)
