
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

    start_button = QPushButton(text='Start Connection')
    start_button.clicked.connect(callbacks['start'])

    address = ('<font color="blue">http://{ip}:2402'    # TODO REMOVE HARD CODED PORT
                '</font color="blue">'.format(ip=get_ip()))
    instructions = (
        '1. Start connection.<br>' +
        '2. On your other device, open ' + address)

    connect_msg = QLabel(text = instructions)

    stop_button = QPushButton(text='Stop Server')
    stop_button.clicked.connect(callbacks['stop'])

    done_button = QPushButton(text = 'Done Transferring')
    done_button.clicked.connect(lambda: window.close())

    open_received = QPushButton(text = 'Open Received...')
    select_to_send = QPushButton(text = 'Select to Send...')

    layout.addWidget(start_button, 0, 0, 1, 2)
    layout.addWidget(connect_msg, 1, 0, 1, 2)
    layout.addWidget(select_to_send, 2, 0, 1, 1)
    layout.addWidget(open_received, 2, 1, 1, 1)
    layout.addWidget(done_button, 3, 0, 1, 2)

    window.setTabOrder(start_button, select_to_send)
    return window
