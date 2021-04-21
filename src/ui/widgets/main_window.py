
from PyQt5.QtWidgets import *


def create_main_window(title: str, start_callback) -> QWidget:
    '''Create the main application window layout.'''
    window = QWidget()
    window.setWindowTitle(title)
    window.setGeometry(0, 0, 400, 300)
    window.move(400, 400)
    layout = QGridLayout(window)

    welcome = QLabel(text='<p>Welcome to Loft!</p>')
    start_button = QPushButton(text='Start Server')
    start_button.clicked.connect(start_callback)

    layout.addWidget(welcome, 0, 0)
    layout.addWidget(start_button, 1, 0)

    window.setTabOrder(start_button, welcome)
    return window
