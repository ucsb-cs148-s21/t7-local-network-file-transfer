
import os
from threading import Thread
import typing

from flask import Flask, render_template
from werkzeug.serving import run_simple

from .inventory import Inventory
from util.file import open_


class Server:
    '''
    Abstract layer over the server.
    '''

    def __init__(self, host: str = 'localhost', port: int = 5000, config: dict = {}):
        # the flask WSGI application
        self.flask: Flask = Flask(__name__)
        self.flask.config.update(config)
        self.flask.secret_key = 'bf7fe7847aa5f10778de0340d4b7cb5163d2727f95801ba0'

        self.thread: Thread = Thread(target=lambda: run_simple(
            host, port, self.flask), daemon=True)

        self.host = host
        self.port = port

        # A dictionary of the available files for download.
        self.available: Inventory = Inventory()

        self.flask.register_error_handler(
            404, lambda err: (render_template('404.html'), str(err)))

    def run(self):
        '''Run the server.'''
        self.register()
        if not self.thread.is_alive():
            self.thread.start()

    def add_sends(self, paths: typing.List[str]):
        '''Add files to send.'''
        for path in paths:
            self.available.add(path)

    def stop(self):
        '''TODO: Stop the server.'''

    def open_downloads(self):
        '''Open the Downloads folder.'''
        open_(self.flask.config['downloads_folder'])

    def register(self):
        '''Register blueprints and resources.'''
        from .blueprints import api, landing

        self.flask.register_blueprint(landing())
        self.flask.register_blueprint(api(self.available))
