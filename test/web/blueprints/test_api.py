
from io import BytesIO
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


def test_post():
    config = DebugConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        dest = config.DOWNLOADS_FOLDER / 'test.txt'
        assert not dest.exists()

        response: Response = c.post('/api/files', data={
            'upload': (BytesIO('lorum ipsum dolor sit amet'.encode('utf8')), 'test.txt')
        })
        assert response.status_code == 200

        assert dest.exists()
        with open(dest, 'r') as f:
            assert f.read() == 'lorum ipsum dolor sit amet'

        dest.unlink()


def test_post_duplicate_filename():
    config = DebugConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        with (config.DOWNLOADS_FOLDER / 'test.txt').open('w') as f:
            f.write('hello')

        dest = config.DOWNLOADS_FOLDER / 'test_1.txt'
        assert not dest.exists()

        response: Response = c.post('/api/files', data={
            'upload': (BytesIO('lorum ipsum dolor sit amet'.encode('utf8')), 'test.txt')
        })
        assert response.status_code == 200

        assert dest.exists()
        with open(dest, 'r') as f:
            assert f.read() == 'lorum ipsum dolor sit amet'

        dest.unlink()


def test_post_empty_filename():
    config = DebugConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        dest = config.DOWNLOADS_FOLDER / 'Untitled'
        assert not dest.exists()

        response: Response = c.post('/api/files', data={
            'upload': (BytesIO('lorum ipsum dolor sit amet'.encode('utf8')), '')
        })
        assert response.status_code == 200

        assert dest.exists()
        with open(dest, 'r') as f:
            assert f.read() == 'lorum ipsum dolor sit amet'

        dest.unlink()


def test_list():
    config = DebugConfig()
    i = IdMap()
    i.add(Path('parent/foo.ext'))
    i.add(Path('parent/bar.ext2'))

    with client(config, api(i)) as c:
        response = c.get('/api/files')
        data = response.get_json()
        assert 'available' in data
        assert len(data['available']) == 2
        assert data['available'][0][0] == 0
        assert data['available'][0][1] == 'foo.ext'
        assert data['available'][1][0] == 1
        assert data['available'][1][1] == 'bar.ext2'


def test_list_empty():
    config = DebugConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        response = c.get('/api/files')
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
            l_r: Response = c.get('/api/files')
            l_data = l_r.get_json()
            assert 'available' in l_data
            assert len(l_data['available']) == 1
            assert l_data['available'][0][0] == 0
            assert l_data['available'][0][1] == path.name

            response: Response = c.get('/api/files/0')

            assert response.status_code == 200
            f.seek(0)
            assert response.get_data(as_text=True) == f.read()


def test_get_empty():
    config = DebugConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        response: Response = c.get('/api/files/0')
        assert response.status_code == 404
