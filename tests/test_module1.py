import unittest
from isNumberFour.main import isNumberFour

class TestIsNumberFour(unittest.TestCase):
    def test_isNumberFour1(self):
        self.assertEqual(isNumberFour(4), True)
    
    def test_isNumberFour2(self):
        self.assertEqual(isNumberFour('4'), True)

if __name__ == "__main__":
    unittest.main()