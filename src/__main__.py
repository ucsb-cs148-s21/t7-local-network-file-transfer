
import os

from __init__ import APP_NAME, DOCUMENTS_FOLDER, DOWNLOADS_FOLDER, HOST, PORT
from ui import Gui

DOCUMENTS_FOLDER = os.path.expanduser(DOCUMENTS_FOLDER)
DOWNLOADS_FOLDER = os.path.expanduser(DOWNLOADS_FOLDER)


def main():
    '''Entry point for the application.'''

    if not os.path.exists(DOWNLOADS_FOLDER):
        os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)

    gui = Gui(APP_NAME, HOST, PORT, {
              'documents_folder': DOCUMENTS_FOLDER, 'downloads_folder': DOWNLOADS_FOLDER})
    gui.run_and_exit()


if __name__ == '__main__':
    main()
