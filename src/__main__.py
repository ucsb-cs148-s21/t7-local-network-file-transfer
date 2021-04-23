import sys
import webbrowser
from flask import Flask, render_template, request
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QWidget
from threading import Thread
from werkzeug.serving import run_simple

APP_NAME = 'loft'
HOST = '0.0.0.0'
PORT = 2402

gui = QApplication(sys.argv)
app = Flask(APP_NAME)

def start_server():
    webbrowser.open('http://localhost:{}'.format(PORT))
    run_simple(HOST, PORT, app) 

def stop_server(server_thread):
    # request.environ.get('werkzeug.server.shutdown')()
    # server_thread.terminate()
    pass

def start_process_server():
    server = Thread(target=start_server, daemon=True)   # Run as daemon so that closing kills server.
    server.start()

def host_gui(): 
    window = QWidget()
    window.setWindowTitle('loft')
    window.setGeometry(0, 0, 400, 300)
    window.move(400, 400)

    hello = QLabel('<i>hello</i>, world')

    start_button = QPushButton(text='start server', parent=window)
    start_button.clicked.connect(start_process_server)

    stop_button = QPushButton(text='stop server', parent=window)
    # stop_button.clicked.connect(stop_server(server_thread))

    stop_msg = QLabel('Stop Button above does not work.\nClose window to stop serving.')

    label=QLabel()
    label.setText('<a href="http://localhost:2402/">Click to open client web interface</a>')    ## Remove hardcoded link
    label.setOpenExternalLinks(True)

    layout = QGridLayout(window)
    layout.addWidget(hello, 0, 0)
    layout.addWidget(start_button, 1, 0)
    layout.addWidget(stop_button, 2, 0)
    layout.addWidget(stop_msg, 3, 0)
    layout.addWidget(label, 4, 0)

    window.show()
    sys.exit(gui.exec_())

def main():
    host_gui()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quit')
def quit_server():
    request.environ.get('werkzeug.server.shutdown')()
    return 'good-bye'

if __name__ == '__main__':
    main()
