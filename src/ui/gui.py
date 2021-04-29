
import sys

from PyQt5.QtWidgets import *

from web import Server
from .widgets import create_main_window


class Gui:
    '''
    Wrapper class handling the GUI.
    '''

    def __init__(self, name: str, *args, **kwargs):
        '''
        Initialize the native GUI. Requires the host and port for the server to
        listen on.
        '''
        self.server = Server(*args, **kwargs)
        self.gui = QApplication(sys.argv)

        self.main_window = create_main_window(name, {
            'start': self.server.run,
            'stop': self.server.stop,
            'open_downloads': self.server.open_downloads,
        })
        self.main_window.show()

    def run_and_exit(self):
        '''Run the GUI.'''
        # if we want PyQt4 compat, replace with `sys.exit(self.main_window.exec_())`
        self.gui.exec()
