from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data)


if __name__ == '__main__':
    app.run(port=1234)
