
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QTextEdit, QWidget


from loft.ui.widgets.qr_code import QrCodeContainer
from loft.util.id_map import IdMap
from loft.util.net import get_ip_thru_gateway as get_ip
from loft.util.rand_pass import generate_random

from loft.config import Config


class MainWindow(QWidget):
    '''
    The main application window.
    '''

    def __init__(self, gui, title: str):
        QWidget.__init__(self)
        self.gui = gui
        self.setWindowTitle(title)

        self.setGeometry(0, 0, 400, 500)
        self.move(400, 400)
        # Keep the window on top so that user remembers to close when they're done
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.layout = QGridLayout(self)

        self.setup()

    def setup(self):
        self.qr_code = QrCodeContainer(get_ip(), self.gui.server.config.PORT)

        Config.PASSWORD["password"] = str(generate_random())

        username = QLineEdit("loft")
        username.setReadOnly(True)
        password = QLineEdit(Config.PASSWORD['password'])
        password.setReadOnly(True)
        password.setEchoMode(QLineEdit.Password)

        password_show_button = QPushButton(text='Show Password')
        password_show_button.setCheckable(True)

        def password_visibility():
            if (password_show_button.isChecked()):
                password.setEchoMode(QLineEdit.Normal)
                password_show_button.setText("Hide Password")
            else:
                password.setEchoMode(QLineEdit.Password)
                password_show_button.setText("Show Password")

        password_show_button.clicked.connect(password_visibility)

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
        select_to_send.clicked.connect(
            lambda: self.select_file(self, file_list))

        file_list: QGroupBox = build_file_list()

        toggle_https = QPushButton(text='Toggle HTTPS')
        # toggle_https.setCheckable(True)
        toggle_https.setDisabled(True)

        def toggle_https_callback():
            '''Toggle HTTPS on the server configuration.'''
            self.gui.server.config.https = not self.gui.server.config.https
            self.qr_code.set_protocol(
                'https' if self.gui.server.config.https else 'http')

        toggle_https.toggled.connect(toggle_https_callback)

        full_instr = QLabel(
            '<a href=https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/blob/main/docs/MANUAL.md>Full Instructions</a>')
        full_instr.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse)
        full_instr.setOpenExternalLinks(True)

        self.layout.addLayout(self.qr_code, 0, 0, 1, 4)

        security_box = QGroupBox("Security")
        security_grid = QGridLayout()
        security_box.setLayout(security_grid)

        security_grid.addWidget(QLabel("User Name:"), 0, 0, 1, 1)
        security_grid.addWidget(username, 0, 1, 1, 1)
        security_grid.addWidget(QLabel("Password:"), 1, 0, 1, 1)
        security_grid.addWidget(password, 1, 1, 1, 1)
        security_grid.addWidget(password_show_button, 2, 0, 1, 2)
        security_grid.addWidget(toggle_https, 3, 0, 1, 2)

        self.layout.addWidget(security_box, 1, 0)

        transfer_box = QGroupBox("Transfer")
        transfer_grid = QGridLayout()
        transfer_box.setLayout(transfer_grid)

        transfer_grid.addWidget(start_button, 0, 0, 1, 2)
        transfer_grid.addWidget(select_to_send, 1, 0, 1, 1)
        transfer_grid.addWidget(open_received, 1, 1, 1, 1)
        transfer_grid.addWidget(done_button, 2, 0, 1, 2)
        transfer_grid.addWidget(file_list, 3, 0, 1, 2)

        self.layout.addWidget(transfer_box, 2, 0)
        self.layout.addWidget(full_instr, 6, 0, 1, 2)

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
