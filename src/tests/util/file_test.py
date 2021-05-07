from ...util.file import dup_name

class Test_dup_name:
    def test_dup_name_no_dups(self):
        assert(dup_name("test.txt", 0)) == "test.txt"
    
    def test_dup_name_one_dup(self):
        assert(dup_name("test.txt", 1)) == "test_1.txt"

    def test_dup_name_two_dup(self):
        assert(dup_name("test.txt", 2)) == "test_2.txt"
