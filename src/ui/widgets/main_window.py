
from PyQt5.QtWidgets import *

def create_main_window(title: str, callbacks) -> QWidget:
    '''
    Create the main application window layout.

    Accepts a dictionary of callbacks, with the following names:
    - `start`: "Start Server" button
    - `stop`: "Stop Server" button
    - `link`: "Open Server Page" button
    '''
    window = QWidget()
    window.setWindowTitle(title)
    window.setGeometry(0, 0, 400, 300)
    window.move(400, 400)
    layout = QGridLayout(window)

    welcome = QLabel(text='<p>Welcome to Loft! This is the Host device.</p>')
    start_button = QPushButton(text='Start Server')
    start_button.clicked.connect(callbacks['start'])

    stop_button = QPushButton(text='Stop Server')
    stop_button.clicked.connect(callbacks['stop'])

    open_server_button = QPushButton(text='Open Server Page')
    open_server_button.clicked.connect(callbacks['link'])

    connect_msg = QLabel(text='Connect by opening a browser on the client device and going to \nhttp://'+get_connect_info())

    layout.addWidget(welcome, 0, 0)
    layout.addWidget(start_button, 1, 0)
    layout.addWidget(stop_button, 2, 0)
    layout.addWidget(open_server_button, 3, 0)
    layout.addWidget(connect_msg, 4, 0)

    window.setTabOrder(start_button, welcome)
    return window

def get_connect_info():
    # from ...__init__ import PORT
    from utils import getIP
    # return(getIP.get_ip_thru_gateway() + string(PORT))
    return (getIP.get_ip_thru_gateway() + ":2402")


