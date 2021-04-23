
import sys

from PyQt5.QtWidgets import *

from web import Server
from .widgets import create_main_window


class Gui:
    '''
    Wrapper class handling the GUI.
    '''

    def __init__(self, name: str, host: str = 'localhost', port: int = 5000):
        '''
        Initialize the native GUI. Requires the host and port for the server to
        listen on.
        '''
        self.server = Server(host, port)
        self.gui = QApplication(sys.argv)

        self.main_window = create_main_window(name, {
            'start': self.server.run,
            'stop': self.server.stop,
            'link': self.server.open_index_in_browser,
        })
        self.main_window.show()

    def run_and_exit(self):
        '''Run the GUI.'''
        # if we want PyQt4 compat, replace with `sys.exit(self.main_window.exec_())`
        self.gui.exec()
