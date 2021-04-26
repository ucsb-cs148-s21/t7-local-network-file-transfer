
import os

from __init__ import APP_NAME, SEND_FOLDER, RECEIVE_FOLDER, HOST, PORT
from ui import Gui

SEND_FOLDER = os.path.expanduser(SEND_FOLDER)
RECEIVE_FOLDER = os.path.expanduser(RECEIVE_FOLDER)

def main():
    '''Entry point for the application.'''
    if not os.path.exists(SEND_FOLDER):
        os.makedirs(SEND_FOLDER, exist_ok=True)

    if not os.path.exists(RECEIVE_FOLDER):
        os.makedirs(RECEIVE_FOLDER, exist_ok=True)

    gui = Gui(APP_NAME, HOST, PORT, {'receive_folder': RECEIVE_FOLDER})
    gui.run_and_exit()


if __name__ == '__main__':
    main()
