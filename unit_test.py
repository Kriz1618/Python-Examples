import unittest
from unittest.mock import mock_open, patch
import pdb

def cube_root(num: int) -> int:
    pdb.set_trace()
    return num ** 3

def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents

class TestingCubeRoot(unittest.TestCase):
    result = 0
    
    def setUp(self) -> None:
        result = 0
        
    def test_positive_cube(self):
        result = cube_root(2)
        self.assertEqual(result, 8)
        
    def test_negative_result(self):
        result = cube_root(-3)
        self.assertEqual(result, -27)
        self.assertNotEqual(result, 27)


class TestReadFileContents(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='Hello, world!')
    def test_read_file(self, mock_file):
        contents = read_file('test.txt')
        mock_file.assert_called_once_with('test.txt', 'r')
        self.assertEqual(contents, 'Hello, world!')   
        

class TestStringMethods(unittest.TestCase):
    first = 0
    second = 0
    
    def setUp(self):
        print('setUp')
        self.first = 6
        self.second = 4
    
    def test_adding(self):
        self.first = 10
        self.assertGreaterEqual(self.first, self.second + 5)
        
    def test_resting(self):
        self.assertLessEqual(self.first, self.second + 3)
        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestingWithBreakpoints(unittest.TestCase):
    
    def tets_breakpoint(self):
       x = cube_root(10)
       pdb.set_trace()
       self.assertEqual(x, 20)
       
if __name__ == '__main__':
    """Just a basic example using unittest modules"""
    unittest.main()
    
