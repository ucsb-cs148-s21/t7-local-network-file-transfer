
from pathlib import Path

from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from loft.util.file import open_
from loft.util.id_map import IdMap
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

    start_button = QPushButton(text='Start Connection')
    start_button.setCheckable(True)
    start_button.toggled.connect(gui.server.run)
    start_button.toggled.connect(lambda: start_button.setDisabled(True))
    # start_button.toggled.connect(lambda: select_to_send.setDisabled(True))

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

    file_list: QGroupBox = build_file_list()

    select_to_send = QPushButton(text='Send Files…')
    select_to_send.clicked.connect(lambda: select_file(window, file_list, gui))

    full_instr = QLabel(
        '<a href=https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/blob/main/usage.md>Full Instructions</a>')
    full_instr.setTextInteractionFlags(
        QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
    full_instr.setOpenExternalLinks(True)

    layout.addWidget(connect_msg, 0, 0, 1, 2)
    layout.addWidget(start_button, 1, 0, 1, 2)
    layout.addWidget(select_to_send, 2, 0, 1, 1)
    layout.addWidget(open_received, 2, 1, 1, 1)
    layout.addWidget(file_list, 3, 0, 1, 1)
    layout.addWidget(done_button, 4, 0, 1, 2)
    layout.addWidget(full_instr)

    window.setTabOrder(start_button, select_to_send)
    window.setTabOrder(select_to_send, open_received)
    window.setTabOrder(open_received, done_button)
    window.setTabOrder(done_button, full_instr)

    return window


def build_file_list() -> QGroupBox:
    '''Create the file list.'''

    return QLabel(text='No files selected.')


def update_file_list(file_list: QWidget, available: IdMap[Path]):
    '''Update the given file list.'''
    if available.size() < 1:
        contents = 'No files selected.'
    else:
        contents = 'To Send:\n'
        for _id, name in available.items():
            contents += '\t' + name.name + '\n'

    file_list.setProperty('text', contents)


def select_file(window: QWidget, file_list: QWidget, gui):
    '''Callback for file selection.'''
    gui.send_file_dialog(window)
    update_file_list(file_list, gui.server.available)
