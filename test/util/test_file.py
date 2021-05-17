
from loft.util.file import split_filename, dup_name


class TestSplitFileName:
    def test_empty(self):
        assert split_filename('') == ('', '')

    def test_no_extensions(self):
        assert split_filename('test') == ('test', '')

    def test_one_extension(self):
        assert split_filename('test.txt') == ('test', '.txt')

    def test_multiple_extensions(self):
        assert split_filename('test.tar.gz') == ('test', '.tar.gz')
        assert split_filename('foo.bar.baz.quo') == ('foo', '.bar.baz.quo')

    def test_leading_dot_with_no_extensions(self):
        assert split_filename('.test') == ('.test', '')

    def test_leading_dot_with_one_extension(self):
        assert split_filename('.test.txt') == ('.test', '.txt')

    def test_leading_dot_with_multiple_extensions(self):
        assert split_filename('.test.tar.gz') == ('.test', '.tar.gz')
        assert split_filename('.foo.bar.baz.quo') == ('.foo', '.bar.baz.quo')


class TestDuplicateNameGeneration:
    def test_no_suffix_for_zero_duplicates(self):
        assert dup_name('test.txt', 0) == 'test.txt'
        assert dup_name('test', 0) == 'test'
        assert dup_name('.test.txt', 0) == '.test.txt'

    def test_suffix_with_extension(self):
        assert dup_name('test.txt', 1) == 'test_1.txt'
        assert dup_name('test.txt', 2) == 'test_2.txt'

    def test_suffix_with_multiple_dots(self):
        assert dup_name('.test.txt', 1) == '.test_1.txt'
        assert dup_name('test.tar.gz', 2) == 'test_2.tar.gz'

    def test_suffix_without_extension(self):
        assert dup_name('test', 1) == 'test_1'
        assert dup_name('test', 2) == 'test_2'
