
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget


from loft.ui.widgets.qr_code import QrCodeContainer
from loft.util.file import open_
from loft.util.id_map import IdMap
from loft.util.net import get_ip_thru_gateway as get_ip


class MainWindow(QWidget):
    '''
    The main application window.
    '''

    def __init__(self, gui, title: str):
        QWidget.__init__(self)
        self.gui = gui
        self.setWindowTitle(title)

        self.setGeometry(0, 0, 400, 300)
        self.move(400, 400)
        # Keep the window on top so that user remembers to close when they're done
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.layout = QGridLayout(self)

        self.setup()

    def setup(self):
        self.qr_code = QrCodeContainer(get_ip(), self.gui.server.config.PORT)
        start_button = QPushButton(text='Start Connection')
        start_button.setCheckable(True)

        def start_connection_callback():
            '''
            Callback for starting the connection. Initializes the server and
            disables buttons that should not be used after server startup.
            '''
            self.gui.server.init()
            start_button.setDisabled(True)
            toggle_https.setDisabled(True)
            self.gui.server.run()

        start_button.toggled.connect(start_connection_callback)

        done_button = QPushButton(text='Done Transferring')
        done_button.clicked.connect(self.close)

        open_received = QPushButton(text='Open Downloads')
        open_received.clicked.connect(self.gui.server.open_downloads)

        select_to_send = QPushButton(text='Send Files…')
        select_to_send.clicked.connect(lambda: self.select_file(self, file_list))

        file_list: QGroupBox = build_file_list()

        toggle_https = QPushButton(text='Toggle HTTPS')
        toggle_https.setCheckable(True)

        def toggle_https_callback():
            '''Toggle HTTPS on the server configuration.'''
            self.gui.server.config.https = not self.gui.server.config.https
            self.qr_code.set_protocol(
                'https' if self.gui.server.config.https else 'http')

        toggle_https.toggled.connect(toggle_https_callback)

        full_instr = QLabel(
            '<a href=https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/blob/main/usage.md>Full Instructions</a>')
        full_instr.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse)
        full_instr.setOpenExternalLinks(True)

        self.layout.addLayout(self.qr_code, 0, 0, 1, 2)

        self.layout.addWidget(select_to_send, 1, 0, 1, 1)
        self.layout.addWidget(open_received, 1, 1, 1, 1)
        self.layout.addWidget(toggle_https, 2, 0, 1, 2)
        self.layout.addWidget(start_button, 3, 0, 1, 2)
        self.layout.addWidget(file_list, 4, 0, 1, 1)
        self.layout.addWidget(done_button, 5, 0, 1, 2)
        self.layout.addWidget(full_instr)

    def select_file(self, window: QWidget, file_list: QWidget):
        '''Callback for file selection.'''
        self.gui.send_file_dialog(window)
        update_file_list(file_list, self.gui.server.available)


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
