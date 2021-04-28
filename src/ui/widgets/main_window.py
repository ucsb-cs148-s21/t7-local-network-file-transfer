
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

    address = ('<font color="blue">http://{ip}:2402'    # TODO REMOVE HARD CODED PORT
                '</font color="blue">'.format(ip=get_ip()))
    instructions = (
        'On your other device, open a browser and go to ' + address)

    connect_msg = QLabel(instructions)

    stop_button = QPushButton(text='Stop Server')
    stop_button.clicked.connect(callbacks['stop'])

    open_server_button = QPushButton(text='Open Server Page')
    open_server_button.clicked.connect(callbacks['link'])

    layout.addWidget(welcome, 0, 0)
    layout.addWidget(start_button, 1, 0)
    layout.addWidget(connect_msg, 2, 0)
    layout.addWidget(stop_button, 3, 0)
    layout.addWidget(open_server_button, 4, 0)

    window.setTabOrder(start_button, welcome)
    return window
