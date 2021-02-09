
import folder_scanning
import unittest

class test_folder_scanning(unittest.TestCase):
    def setUp(self):
        # This function is called before every test
        self.fs = folder_scanning.folder_scanning_tool()
    
    def test_001(self):
        # Correct case
        self.fs.scan(r"test_data\data1")
        self.fs.importList(r"test_data\list.txt")
        assert(self.fs.compare() == 0)
        
    def test_002(self):
        # A file is missing
        self.fs.scan(r"test_data\data2")
        self.fs.importList(r"test_data\list.txt")
        assert(self.fs.compare() == -1)
        
    def test_003(self):
        # A file is unexpected
        self.fs.scan(r"test_data\data3")
        self.fs.importList(r"test_data\list.txt")
        assert(self.fs.compare() == -2)
        
    def test_004(self):
        # A file is not the right type => missing
        self.fs.scan(r"test_data\data4")
        self.fs.importList(r"test_data\list.txt")
        assert(self.fs.compare() == -1)
    
if __name__ == '__main__':
    unittest.main()