
import unittest

from loft.util.file import split_filename, dup_name


class TestSplitFileName(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(split_filename(''), ('', ''))

    def test_no_extensions(self):
        self.assertEqual(split_filename('test'), ('test', ''))

    def test_one_extension(self):
        self.assertEqual(split_filename('test.txt'), ('test', '.txt'))

    def test_multiple_extensions(self):
        self.assertEqual(split_filename('test.tar.gz'), ('test', '.tar.gz'))
        self.assertEqual(split_filename('foo.bar.baz.quo'),
                         ('foo', '.bar.baz.quo'))

    def test_leading_dot_with_no_extensions(self):
        self.assertEqual(split_filename('.test'), ('.test', ''))

    def test_leading_dot_with_one_extension(self):
        self.assertEqual(split_filename('.test.txt'), ('.test', '.txt'))

    def test_leading_dot_with_multiple_extensions(self):
        self.assertEqual(split_filename('.test.tar.gz'), ('.test', '.tar.gz'))
        self.assertEqual(split_filename('.foo.bar.baz.quo'),
                         ('.foo', '.bar.baz.quo'))


class TestDuplicateNameGeneration(unittest.TestCase):
    def test_no_suffix_for_zero_duplicates(self):
        self.assertEqual(dup_name('test.txt', 0), 'test.txt')
        self.assertEqual(dup_name('test', 0), 'test')
        self.assertEqual(dup_name('.test.txt', 0), '.test.txt')

    def test_suffix_with_extension(self):
        self.assertEqual(dup_name('test.txt', 1), 'test_1.txt')
        self.assertEqual(dup_name('test.txt', 2), 'test_2.txt')

    def test_suffix_with_multiple_dots(self):
        self.assertEqual(dup_name('.test.txt', 1), '.test_1.txt')
        self.assertEqual(dup_name('test.tar.gz', 2), 'test_2.tar.gz')

    def test_suffix_without_extension(self):
        self.assertEqual(dup_name('test', 1), 'test_1')
        self.assertEqual(dup_name('test', 2), 'test_2')


if __name__ == '__main__':
    unittest.main()
