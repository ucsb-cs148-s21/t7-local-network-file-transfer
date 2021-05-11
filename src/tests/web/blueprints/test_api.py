
import unittest
from unittest.mock import MagicMock

from flask import Blueprint, Flask
from flask.testing import FlaskClient
from flask.wrappers import Response

from ....config import TestingConfig
from ....web.blueprints.api import api
from ....web.inventory import Inventory


def client(api: Blueprint) -> FlaskClient[Response]:
    '''
    Create the test Flask application, register the blueprint and return the
    Flask test client.
    '''
    flask = Flask(__name__)
    flask.config.from_object(TestingConfig())
    flask.register_blueprint(api)
    return flask.test_client()


class TestApi(unittest.TestCase):
    def test_list(self):
        i = Inventory()
        i.add('foo')
        i.add('bar')

        with client(api(i)) as c:
            response = c.open('/api', method='LIST')
            data = response.get_json()
            self.assertIn('available', data)
            self.assertEqual(data['available'][0], 'foo')
            self.assertEqual(data['available'][1], 'bar')
            self.assertEqual(len(data['available']), 2)


if __name__ == '__main__':
    unittest.main()
