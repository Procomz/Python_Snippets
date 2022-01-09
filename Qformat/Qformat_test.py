# -*- coding: utf-8 -*-
import sys
import unittest

from Qformat import Qformat

class QformatTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(QformatTest, self).__init__(*args, **kwargs)
        self.q = Qformat()
        
    def test_floatToQ1516(self):
        self.assertEqual(self.q.floatToQ1516(1.5), '0x18000')
        self.assertEqual(self.q.floatToQ1516(1.75), '0x1c000')
        self.assertEqual(self.q.floatToQ1516(1.0), '0x10000')
        self.assertEqual(self.q.floatToQ1516(64.0), '0x400000')
        
        self.assertEqual(self.q.floatToQ1516(-1.0), '-0x10000')
        
    def test_Q1516ToFloat(self):
        self.assertEqual(self.q.Q1516ToFloat(0x18000), 1.5)
        self.assertEqual(self.q.Q1516ToFloat(0x1c000), 1.75)
        self.assertEqual(self.q.Q1516ToFloat(0x10000), 1.0)
        self.assertEqual(self.q.Q1516ToFloat(0x400000), 64.0)
     
        
if __name__ == "__main__":
    print("Testing Qformat")
    print("Running on : " + sys.version)
    unittest.main()