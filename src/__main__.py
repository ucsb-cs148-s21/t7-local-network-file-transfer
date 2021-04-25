
import os

from __init__ import APP_NAME, APP_FOLDER, RECEIVED_FOLDER, HOST, PORT
from ui import Gui

APP_FOLDER = os.path.expanduser(APP_FOLDER)
RECEIVED_FOLDER = os.path.expanduser(RECEIVED_FOLDER)

def main():
    '''Entry point for the application.'''
    if not os.path.exists(APP_FOLDER):
        os.mkdir(APP_FOLDER)

    if not os.path.exists(RECEIVED_FOLDER):
        os.mkdir(RECEIVED_FOLDER)

    gui = Gui(APP_NAME, HOST, PORT, {'received_folder': RECEIVED_FOLDER})
    gui.run_and_exit()


if __name__ == '__main__':
    main()
