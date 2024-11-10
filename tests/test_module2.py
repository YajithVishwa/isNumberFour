import unittest
from isNumberFour.main import isNumberFour

class TestIsNumberFour(unittest.TestCase):
    def test_isNotNumberFour1(self):
        self.assertEqual(isNumberFour(5), False)

    def test_isNotNumberFour2(self):
        self.assertEqual(isNumberFour('5'), False)

if __name__ == "__main__":
    unittest.main()