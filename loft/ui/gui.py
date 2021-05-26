
from pathlib import Path
import sys
import qrcode

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from loft.config import Config
from loft.web import Server
from loft.ui.widgets import create_main_window
# from loft.ui.widgets.qrcode import Window
# from loft.ui.widgets.qrcode import Image


class Gui:
    '''
    Wrapper class handling the GUI.
    '''

    def __init__(self, config: Config, *args, **kwargs):
        '''
        Initialize the native GUI. Requires the host and port for the server to
        listen on.
        '''

        self.server = Server(config, *args, **kwargs)
        self.gui = QApplication(sys.argv)

        self.main_window = create_main_window(config.APP_NAME, self)
        self.main_window.show()
        
  

    def run_and_exit(self):
        '''Run the GUI.'''
        # if we want PyQt4 compat, replace with `sys.exit(self.main_window.exec_())`
        self.gui.exec()

    def send_file_dialog(self, parent: QWidget = None):
        '''Open up the file dialog to select files to send.'''
        file_, _ = QFileDialog.getOpenFileName(parent, 'Select File to Send',
                                               str(self.server.config.DOCUMENTS_FOLDER))
        self.server.add_sends(Path(file_))

        # files, _ = QFileDialog.getOpenFileNames(parent, 'Select Files to Send',
        #                                         str(self.server.config.DOCUMENTS_FOLDER))
        # self.server.add_sends(Path(files))