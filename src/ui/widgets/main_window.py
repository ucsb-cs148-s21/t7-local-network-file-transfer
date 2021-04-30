import os
from PyQt5.QtWidgets import *
from util.net import get_ip_thru_gateway as get_ip


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

    open_received = QPushButton(text = 'Open Downloads')
    select_to_send = QPushButton(text = 'Select Files to Send...')

    def select():
        documents = os.path.expanduser('~{}Documents'.format(os.sep))
        file_name_tuple = QFileDialog.getOpenFileName(None, 'Select File to Send', documents)
        file_name = os.path.basename(file_name_tuple[0])
        file_path = os.path.dirname(file_name_tuple[0])
        file_path_with_slash = os.path.join(file_path, '')
        print('File path is:', file_path_with_slash)
        print('File name is:', file_name)
        callbacks['set_send_file_name_address']([file_name, file_path])


    select_to_send.clicked.connect(select)

    layout.addWidget(start_button, 0, 0, 1, 2)
    layout.addWidget(connect_msg, 1, 0, 1, 2)
    layout.addWidget(select_to_send, 2, 0, 1, 1)
    layout.addWidget(open_received, 2, 1, 1, 1)
    layout.addWidget(done_button, 3, 0, 1, 2)


    window.setTabOrder(start_button, select_to_send)
    return window
