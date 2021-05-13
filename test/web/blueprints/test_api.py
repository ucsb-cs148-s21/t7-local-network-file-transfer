
from io import FileIO
from pathlib import Path
import random

from flask import Blueprint, Flask
import pytest

from loft.config import Config, DebugConfig
from loft.util.id_map import IdMap
from loft.web.blueprints.api import api


def tempfile(dir_: Path) -> FileIO:
    '''
    Create our own temporary file. The tempfile files have permissions issues.
    '''
    return open(dir_ / 'temp.txt', 'w+')


def client(config: Config, api: Blueprint):
    '''
    Create the test Flask application, register the blueprint and return the
    Flask test client.
    '''
    flask = Flask(__name__)
    flask.config.from_object(config)
    flask.register_blueprint(api)
    return flask.test_client()


def test_list():
    config = DebugConfig()
    i = IdMap()
    i.add(Path('parent/foo.ext'))
    i.add(Path('parent/bar.ext2'))

    with client(config, api(i)) as c:
        response = c.open('/api', method='LIST')
        data = response.get_json()
        assert 'available' in data
        assert len(data['available']) == 2
        assert data['available']['0'] == 'foo.ext'
        assert data['available']['1'] == 'bar.ext2'


def test_list_empty():
    config = DebugConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        response = c.open('/api', method='LIST')
        data = response.get_json()
        assert 'available' in data
        assert len(data['available']) == 0


def test_get():
    config = DebugConfig()
    i = IdMap()

    rand = random.Random()
    rand.seed()

    with open(config.DOCUMENTS_FOLDER / 'a.txt', 'w+') as f:
        for _ in range(1, 10):
            f.write(str(rand.uniform(0, 1000)))

        assert i.add(Path(f.name)) == 0

        with client(config, api(i)) as c:
            response = c.get('/api?id=0')


def test_get_empty():
    config = DebugConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        pass
