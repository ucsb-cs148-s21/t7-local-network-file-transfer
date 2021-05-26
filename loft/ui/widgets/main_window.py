
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from loft.util.net import get_ip_thru_gateway as get_ip


def create_main_window(title: str, gui) -> QWidget:
    '''
    Create the main application window layout.
    '''
    window = QWidget()
    window.setWindowTitle(title)
    window.setGeometry(0, 0, 400, 300)
    window.move(400, 400)
    # Keep the window on top so that user remembers to close when they're done
    window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    layout = QGridLayout(window)

    def start_connection_callback():
        '''
        Callback for starting the connection. Initializes the server and
        disables buttons that should not be used after server startup.
        '''
        gui.server.init()
        start_button.setDisabled(True)
        toggle_https.setDisabled(True)
        gui.server.run()

    start_button = QPushButton(text='Start Connection')
    start_button.setCheckable(True)
    start_button.toggled.connect(start_connection_callback)

    connect_msg = QLabel(text='''
Note: Send file cannot be modified after starting.<br />
Please Close Loft and restart to make changes.
<ol>
    <li>Select Send Files if sending.</li>
    <li>Start Connection.</li>
    <li>On your other device, open <font color="#0000ee">http://{}:{}</font>.</li>
    <li>Close Loft after transfering.</li>
</ol>
'''.format(get_ip(), gui.server.config.PORT))

    done_button = QPushButton(text='Done Transferring')
    done_button.clicked.connect(window.close)

    open_received = QPushButton(text='Open Downloads')
    open_received.clicked.connect(gui.server.open_downloads)

    select_to_send = QPushButton(text='Send Files…')
    select_to_send.clicked.connect(lambda: gui.send_file_dialog(window))

    toggle_https = QPushButton(text='Toggle HTTPS')
    toggle_https.setCheckable(True)
    toggle_https.toggled.connect(lambda: toggle_https_callback(gui))

    full_instr = QLabel(
        '<a href=https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/blob/main/usage.md>Full Instructions</a>')
    full_instr.setTextInteractionFlags(
        QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
    full_instr.setOpenExternalLinks(True)

    layout.addWidget(connect_msg, 0, 0, 1, 2)
    layout.addWidget(select_to_send, 1, 0, 1, 1)
    layout.addWidget(open_received, 1, 1, 1, 1)
    layout.addWidget(toggle_https, 2, 0, 1, 2)
    layout.addWidget(start_button, 3, 0, 1, 2)
    layout.addWidget(done_button, 4, 0, 1, 2)
    layout.addWidget(full_instr)

    window.setTabOrder(select_to_send, open_received)
    window.setTabOrder(open_received, start_button)
    window.setTabOrder(start_button, toggle_https)
    window.setTabOrder(toggle_https, done_button)
    window.setTabOrder(done_button, full_instr)
    return window


def toggle_https_callback(gui):
    '''Toggle HTTPS on the server configuration.'''
    gui.server.config.https = not gui.server.config.https
