
import os
from threading import Thread

from flask import Flask, render_template
from werkzeug.serving import run_simple

from config import Config
from util.file import open_


class Server:
    '''
    Abstract layer over the server.
    '''

    def __init__(self, config: Config):
        self.config = config

        # the flask WSGI application
        self.flask = Flask(__name__)
        self.flask.config.from_object(config)
        try:
            self.flask.config.from_envvar(config.config_filepath)
        except RuntimeError:    # env var is not set
            pass

        self.thread = Thread(
            target=lambda: run_simple(config.HOST, config.PORT, self.flask), daemon=True)

        # A list containing
        self.send_name_path = {'file_name': '', 'file_path': ''}

        self.flask.register_error_handler(
            404, lambda err: (render_template('404.html'), str(err)))

    def run(self):
        '''Run the server.'''
        register_blueprints(self.flask, self.send_name_path)
        if not self.thread.is_alive():
            self.thread.start()

    def set_send_name_path(self, send_name, send_path):
        self.send_name_path['file_name'] = send_name
        self.send_name_path['file_path'] = send_path

    def stop(self):
        '''TODO: Stop the server.'''

    def open_downloads(self):
        '''Open the Downloads folder.'''
        open_(self.config.downloads_folder)


def register_blueprints(app: Flask, send_name_path):
    '''Register the blueprints for the Flask application.'''
    from .blueprints import create_blueprint

    app.register_blueprint(create_blueprint(send_name_path))
