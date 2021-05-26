
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget


from loft.ui.widgets.qr_code import QrCodeContainer
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
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        self.layout = QGridLayout(self)

        self.setup()

    def setup(self):
        self.qr_code = QrCodeContainer(get_ip(), self.gui.server.config.PORT)
        start_button = QPushButton(text='Start Connection')
        start_button.setCheckable(True)
        start_button.toggled.connect(self.gui.server.run)
        start_button.toggled.connect(lambda: start_button.setDisabled(True))
        start_button.toggled.connect(lambda: select_to_send.setDisabled(True))

        done_button = QPushButton(text='Done Transferring')
        done_button.clicked.connect(self.close)

        open_received = QPushButton(text='Open Downloads')
        open_received.clicked.connect(self.gui.server.open_downloads)

        select_to_send = QPushButton(text='Send Files…')
        select_to_send.clicked.connect(lambda: self.gui.send_file_dialog(self))

        full_instr = QLabel(
            '<a href=https://github.com/ucsb-cs148-s21/t7-local-network-file-transfer/blob/main/usage.md>Full Instructions</a>')
        full_instr.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        full_instr.setOpenExternalLinks(True)

        self.layout.addLayout(self.qr_code, 0, 0, 1, 2)

        self.layout.addWidget(select_to_send, 1, 0, 1, 1)
        self.layout.addWidget(open_received, 1, 1, 1, 1)
        self.layout.addWidget(start_button, 2, 0, 1, 2)
        self.layout.addWidget(done_button, 3, 0, 1, 2)
        self.layout.addWidget(full_instr)
