import unittest
from isNumberFour.module1 import isNumberFour

class TestIsNumberFour(unittest.TestCase):
    def test_isNotNumberFour(self):
        self.assertEqual(isNumberFour(5), False)

if __name__ == "__main__":
    unittest.main()