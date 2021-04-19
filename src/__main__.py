
import sys
import webbrowser

from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QWidget

APP_NAME = 'loft'
HOST = '0.0.0.0'
PORT = 2402

gui = QApplication(sys.argv)
app = Flask(APP_NAME)
server = WSGIServer((HOST, PORT), app)


def start_server(app, window):
    '''Start the web server and close the GUI window.'''
    def callback():
        window.close()
        webbrowser.open('http://localhost:{}'.format(PORT))
        # server.run(host=HOST, port=PORT)
        server.serve_forever()
    return callback


def main():
    window = QWidget()
    window.setWindowTitle('loft')
    window.setGeometry(0, 0, 400, 300)
    window.move(400, 400)

    hello = QLabel('<i>hello</i>, world')

    button = QPushButton(text='start server', parent=window)
    button.clicked.connect(start_server(app, window))

    layout = QGridLayout(window)
    layout.addWidget(hello, 0, 0)
    layout.addWidget(button, 1, 0)

    window.show()
    sys.exit(gui.exec_())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quit')
def quit_server():
    # request.environ.get('werkzeug.server.shutdown')()
    server.stop()
    return 'good-bye'


if __name__ == '__main__':
    main()
