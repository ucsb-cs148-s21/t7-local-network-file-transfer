
import os
from threading import Thread

from flask import Flask
from werkzeug.serving import run_simple


class Server:
    '''
    Abstract layer over the server.
    '''

    def __init__(self, host: str = 'localhost', port: int = 5000, config: dict = {}):
        # the flask WSGI application
        self.flask = Flask(__name__)
        self.flask.config.update(config)
        
        self.thread = Thread(
            target=lambda: run_simple(host, port, self.flask), daemon=True)

        self.send_file_name_address = []

        self.host = host
        self.port = port

    def run(self):
        '''Run the server.'''
        register_blueprints(self.flask, self.send_file_name_address)
        if not self.thread.is_alive():
            self.thread.start()

    def set_send_file_name_address(self, send_file_name_address):
        self.send_file_name_address = send_file_name_address

    def stop(self):
        '''TODO: Stop the server.'''

def register_blueprints(app: Flask, send_file_name_address):
    '''Register the blueprints for the Flask application.'''
    from .blueprints import create_blueprint

    app.register_blueprint(create_blueprint(send_file_name_address))
