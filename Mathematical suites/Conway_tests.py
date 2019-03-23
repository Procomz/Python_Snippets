# -*- coding: utf-8 -*-
import sys
import unittest
from Conway import Conway

class ConwayTest(unittest.TestCase):
    def test_Conway1(self):
        c = Conway('1')
        self.assertEqual(c.getCurrent(), '1')
        self.assertEqual(c.computeNext(), '11')
        self.assertEqual(c.computeNext(), '21')
        self.assertEqual(c.computeNext(), '1211')
        self.assertEqual(c.computeNext(), '111221')
        self.assertEqual(c.computeNext(), '312211')
        self.assertEqual(c.computeNext(), '13112221')
        
        
if __name__ == "__main__":
    print("Testing Conway")
    print("Running on : " + sys.version)
    unittest.main()