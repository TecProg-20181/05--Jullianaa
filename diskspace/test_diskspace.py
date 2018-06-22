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
    
    def test_return_type(self):
        blocks = 0
        bytes_size = bytes_to_readable(blocks)
        self.assertIsInstance(bytes_size, str)

    def test_tbytes(self):
        blocks = 100000000000
        bytes_size = bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Tb', label)

    def test_gbytes(self):
        blocks = 100000000
        bytes_size = bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Gb', label)

if __name__ == '__main__':
    unittest.main()