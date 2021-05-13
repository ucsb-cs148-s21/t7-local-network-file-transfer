
import os

from loft.config import Config
from loft.ui import Gui


def main():
    '''Entry point for the application.'''

    config = Config()

    gui = Gui(config)
    gui.run_and_exit()


if __name__ == '__main__':
    main()
