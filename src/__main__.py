
from __init__ import APP_NAME, HOST, PORT
from ui import Gui


def main():
    '''Entry point for the application.'''
    gui = Gui(APP_NAME, HOST, PORT)
    gui.run_and_exit()


if __name__ == '__main__':
    main()
