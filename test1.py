import unittest

from defs1 import add, sub, mul, div

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_sub(self):
        self.assertEqual(sub(7, 4), 3)
        self.assertNotEqual(sub(4, 2), 1)

    def test_mul(self):
        self.assertNotEqual(mul(2, 5), 12)
        self.assertEqual(mul(3, 6), 18)

    def test_div(self):
        self.assertNotEqual(div(4, 2), 3)
        self.assertEqual(div(20, 5), 4)

if __name__ == '__main__':
    unittest.main()