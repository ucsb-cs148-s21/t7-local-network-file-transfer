
import os

from __init__ import APP_NAME, DOWNLOADS_FOLDER, HOST, PORT
from ui import Gui


DOWNLOADS_FOLDER = os.path.expanduser(DOWNLOADS_FOLDER)

def main():
    '''Entry point for the application.'''
    if not os.path.exists(DOWNLOADS_FOLDER):
        os.mkdir(DOWNLOADS_FOLDER)

    gui = Gui(APP_NAME, HOST, PORT, {'downloads_folder': DOWNLOADS_FOLDER})
    gui.run_and_exit()


if __name__ == '__main__':
    main()
