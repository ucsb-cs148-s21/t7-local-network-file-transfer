
import os

from flask import Flask
from gevent.pywsgi import WSGIServer


class Server:
    '''
    Abstract layer over the server.
    '''

    def __init__(self, host: str, port: int):
        # the flask WSGI application
        self.flask = Flask(__name__)
        self.server = WSGIServer((host, port), self.flask)

        register_blueprints(self.flask)

        self.host = host
        self.port = port

    def run(self):
        '''Run the server.'''
        # TODO: Run in a separate process.

        self.server.serve_forever()

    def stop(self):
        '''Stop the server.'''
        self.server.stop()

    def open_index_in_browser(self):
        '''Open the index in the user's default browser.'''
        import webbrowser
        webbrowser.open('http://localhost:{}'.format(self.port))


def register_blueprints(app: Flask):
    '''Register the blueprints for the Flask application.'''
    from .blueprints import landing

    app.register_blueprint(landing)
