
from pathlib import Path
from threading import Thread
import typing

from flask import Flask, render_template
from werkzeug.serving import run_simple, make_ssl_devcert

from loft.config import Config
from loft.util.file import open_, get_data
from loft.util.id_map import IdMap


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

        certificates: typing.Tuple[str, str] = self.generate_certificates()

        self.thread: Thread = Thread(target=lambda: run_simple(
            config.HOST,
            config.PORT,
            self.flask,
            threaded=True,
            ssl_context=certificates,
        ), daemon=True)

        # A dictionary of the available files for download.
        self.available: IdMap[Path] = IdMap()

        self.flask.register_error_handler(
            404, lambda err: (render_template('404.html'), str(err)))

    def run(self):
        '''Run the server.'''
        self.register()
        if not self.thread.is_alive():
            self.thread.start()

    def add_sends(self, path: Path):
        '''Add a single file to send.'''
        self.available.add(path)

    # def add_sends(self, paths: typing.List[str]):
    #     '''Add files to send.'''
    #     for path in paths:
    #         self.available.add(path)

    def stop(self):
        '''TODO: Stop the server.'''

    def open_downloads(self):
        '''Open the Downloads folder.'''
        open_(self.config.DOWNLOADS_FOLDER)

    def register(self):
        '''Register blueprints and resources.'''
        from .blueprints import api, landing

        self.flask.register_blueprint(landing())
        self.flask.register_blueprint(api(self.available))

    def generate_certificates(self) -> typing.Tuple[str, str]:
        '''Generate SSL certificates if they do not already exist.'''
        data_folder: Path = get_data()

        key_name: str = 'ssl_key'

        cert: Path = Path(data_folder, key_name + '.crt')
        priv: Path = Path(data_folder, key_name + '.key')
        if cert.is_file() and priv.is_file():
            return str(cert), str(priv)

        return make_ssl_devcert(data_folder / 'ssl_key', host=self.config.HOST)
