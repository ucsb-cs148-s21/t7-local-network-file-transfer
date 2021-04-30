
import os
from threading import Thread

from flask import Flask, render_template
from werkzeug.serving import run_simple

from util.file import open_


class Server:
    '''
    Abstract layer over the server.
    '''

    def __init__(self, host: str = 'localhost', port: int = 5000, config: dict = {}):
        # the flask WSGI application
        self.flask = Flask(__name__)
        self.flask.config.update(config)
        self.flask.secret_key = 'bf7fe7847aa5f10778de0340d4b7cb5163d2727f95801ba0'

        self.thread = Thread(
            target=lambda: run_simple(host, port, self.flask), daemon=True)

        self.send_file_name_address = []

        self.host = host
        self.port = port

        self.flask.register_error_handler(
            404, lambda err: (render_template('404.html'), str(err)))

    def run(self):
        '''Run the server.'''
        register_blueprints(self.flask, self.send_file_name_address)
        if not self.thread.is_alive():
            self.thread.start()

    def set_send_file_name_address(self, send_file_name_address):
        self.send_file_name_address = send_file_name_address

    def stop(self):
        '''TODO: Stop the server.'''
    
    def open_downloads(self):
        '''Open the Downloads folder.'''
        open_(self.flask.config['downloads_folder'])


def register_blueprints(app: Flask, send_file_name_address):
    '''Register the blueprints for the Flask application.'''
    from .blueprints import create_blueprint

    app.register_blueprint(create_blueprint(send_file_name_address))
