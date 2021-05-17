
import random
import unittest

from loft.util.id_map import IdMap

rand = random.Random()

rand.seed(24242424)


class TestIdMap(unittest.TestCase):

    def test_add(self):
        i = IdMap()
        self.assertEqual(i.add('foo'), 0, 'First file ID should be 0.')
        self.assertEqual(i.add('bar'), 1, 'Second file ID should be 1.')
        self.assertEqual(i.get(0), 'foo', 'Should be able to get first file '
                         'with ID 0.')
        self.assertEqual(i.get(1), 'bar', 'Should be able to get secondfile '
                         'with ID 1.')

    def test_remove_valid_id(self):
        i = IdMap()
        i.add('foo')
        i.add('bar')
        i.add('baz')

        self.assertTrue(i.contains(1))

        self.assertTrue(i.remove(1))

        self.assertFalse(i.contains(1))
        self.assertIsNone(i.get(1))

    def test_remove_invalid_id(self):
        i = IdMap()
        i.add('foo')
        i.add('bar')

        self.assertFalse(i.remove(42))

    def test_contains(self):
        i = IdMap()
        i.add('foo')
        i.add('bar')
        i.add('baz')

        self.assertTrue(i.contains(0))
        self.assertTrue(i.contains(1))
        self.assertTrue(i.contains(2))
        self.assertFalse(i.contains(3))

        i.add('quo')

        self.assertTrue(i.contains(3))

    def test_size(self):
        i = IdMap()
        self.assertEqual(i.size(), 0)

        i.add('foo')
        i.add('bar')
        self.assertEqual(i.size(), 2)

    def test_get_when_empty(self):
        i = IdMap()
        for _ in range(0, 1_000_000):
            self.assertIsNone(i.get(rand.uniform(0, 1_000_000)),
                              'IdMap.get should return None for any file ID '
                              'when empty.')

    def test_get_invalid_ids(self):
        i = IdMap()
        i.add('foo')
        i.add('bar')

        for _ in range(1, 1_000_000):
            self.assertIsNone(i.get(rand.uniform(2, 1_000_000)),
                              'Getting file IDs outside of the range of '
                              'previously inserted files should result in None.')

    def test_get_and_contains_removed_ids(self):
        i = IdMap()
        i.add('foo')
        i.add('bar')
        i.add('baz')

        self.assertEqual(i.get(1), 'bar')

        i.remove(1)

        self.assertFalse(i.contains(1))
        self.assertIsNone(i.get(1))

    def test_items(self):
        i = IdMap()

        files = ['foo', 'bar', 'baz', 'quo']

        i.add('foo')
        i.add('bar')
        i.add('baz')
        i.add('quo')

        for id_, filename in i.items():
            self.assertEqual(filename, files[id_])


if __name__ == '__main__':
    unittest.main()
