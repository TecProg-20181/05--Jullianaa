import unittest
from diskspace import *

class Diskspace_test(unittest.TestCase):
    
    def test_bytes_readable(self):
        blocks = 0
        result = bytes_to_readable(blocks)
        self.assertEqual('0.00B', result) 

    def test_bytes_readable(self):
        blocks = 1
        result = bytes_to_readable(blocks)
        self.assertEqual('512.00B', result) 
        
if __name__ == '__main__':
    unittest.main()