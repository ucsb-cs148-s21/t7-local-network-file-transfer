
from flask import Blueprint, Flask
from flask.testing import FlaskClient
from flask.wrappers import Response

from loft.config import Config, TestingConfig
from loft.util.id_map import IdMap
from loft.web.blueprints.api import api


def client(config: Config, api: Blueprint) -> FlaskClient[Response]:
    '''
    Create the test Flask application, register the blueprint and return the
    Flask test client.
    '''
    flask = Flask(__name__)
    flask.config.from_object(config)
    flask.register_blueprint(api)
    return flask.test_client()


def test_list():
    config = TestingConfig()
    i = IdMap()
    i.add('foo')
    i.add('bar')

    with client(config, api(i)) as c:
        response = c.open('/api', method='LIST')
        data = response.get_json()
        assert 'available' in data
        assert data['available'][0] == 'foo'
        assert data['available'][1] == 'bar'
        assert len(data['available']) == 2


def test_list_empty():
    config = TestingConfig()
    i = IdMap()

    with client(config, api(i)) as c:
        response = c.open('/api', method='LIST')
        data = response.get_json()
        assert 'available' in data
        assert len(data['available']) == 0
