import unittest
from defs3 import divide

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_fail(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
