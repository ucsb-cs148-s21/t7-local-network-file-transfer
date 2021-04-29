import os
from PyQt5.QtWidgets import *
from .getIP import get_ip_thru_gateway as get_ip

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

    welcome = QLabel(text='Welcome to Loft! This is the Host device.')
    start_button = QPushButton(text='Start Connection')
    start_button.clicked.connect(callbacks['start'])

    connect_msg = QLabel(
        text=('Connection Instructions\n'
        '1. Start Connection\n'
        '2. On your other device, open a browser and go to http://'+ get_ip() + ':2402'))   # TODO REMOVE HARD CODE

    stop_button = QPushButton(text='Stop Server')
    stop_button.clicked.connect(callbacks['stop'])

    open_server_button = QPushButton(text='Open Server Page')
    open_server_button.clicked.connect(callbacks['link'])

    def select():
        fileNameTuple = QFileDialog.getOpenFileName(None, 'Open File!', '.')
        fileName = os.path.basename(fileNameTuple[0])
        filePath = os.path.dirname(fileNameTuple[0])
        filePathWithSlash = os.path.join(filePath, '')
        print('File path is:', filePathWithSlash)
        print('File name is:', fileName)


    select_to_send = QPushButton(text = 'Send File to Other Device')
    select_to_send.clicked.connect(select)

    layout.addWidget(welcome, 0, 0)
    layout.addWidget(start_button, 1, 0)
    layout.addWidget(connect_msg, 2, 0)
    layout.addWidget(select_to_send, 3, 0)
    layout.addWidget(stop_button, 4, 0)
    layout.addWidget(open_server_button, 5, 0)

    window.setTabOrder(start_button, welcome)
    return window
