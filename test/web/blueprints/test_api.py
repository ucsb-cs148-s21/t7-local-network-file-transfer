
from io import FileIO
from pathlib import Path
import random

from flask import Blueprint, Flask
from flask.wrappers import Response

from loft.config import Config, DebugConfig
from loft.util.id_map import IdMap
from loft.web.blueprints.api import api


rand = random.Random()
rand.seed(24242424)


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

    with open(config.DOCUMENTS_FOLDER / 'a.txt', 'w+') as f:
        path = Path(f.name)
        for _ in range(1, 10):
            f.write(str(rand.uniform(0, 1000)))

        assert i.add(path) == 0

        with client(config, api(i)) as c:
            l_r: Response = c.open('/api', method='LIST')
            l_data = l_r.get_json()
            assert 'available' in l_data
            assert len(l_data['available']) == 1
            assert l_data['available']['0'] == path.name

            response: Response = c.get('/api?id=0')

            f.seek(0)
            assert response.get_data(as_text=True) == f.read()


def test_get_empty():
    config = DebugConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        pass
