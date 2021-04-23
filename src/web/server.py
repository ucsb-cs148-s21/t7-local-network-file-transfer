
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

        register_blueprints(self.flask)

        self.host = host
        self.port = port

    def run(self):
        '''Run the server.'''
        if not self.thread.is_alive():
            self.thread.start()

    def stop(self):
        '''TODO: Stop the server.'''

    def open_index_in_browser(self):
        '''Open the index in the user's default browser.'''
        import webbrowser
        webbrowser.open('http://localhost:{}'.format(self.port))


def register_blueprints(app: Flask):
    '''Register the blueprints for the Flask application.'''
    from .blueprints import landing

    app.register_blueprint(landing)
