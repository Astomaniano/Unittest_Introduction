import unittest
from defs2 import check

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertFalse(check(3))
        self.assertFalse(check(57))

if __name__ == '__main__':
    unittest.main()