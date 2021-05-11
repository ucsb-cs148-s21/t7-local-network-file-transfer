
import os

from src.config import Config
from src.ui import Gui


def main():
    '''Entry point for the application.'''

    config = Config()

    if not os.path.exists(config.DOWNLOADS_FOLDER):
        os.makedirs(config.DOWNLOADS_FOLDER, exist_ok=True)

    gui = Gui(config)
    gui.run_and_exit()


if __name__ == '__main__':
    main()
