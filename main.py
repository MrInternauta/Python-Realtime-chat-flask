from flask import Flask, render_template
from flask_socketio import SocketIO, send

#Inicializa servidor
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
#Inicializar socket con el servidor
socketio = SocketIO(app)
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_Message(msg):
    print(msg)
    send(msg, broadcast = True)

#inicializar servidor
if __name__ == '__main__':
    socketio.run(app)
