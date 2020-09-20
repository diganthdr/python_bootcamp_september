#unittests, pytest
import unittest #inbuilt
from calc import calc_add

class TestCalculator(unittest.TestCase):
# Inputs, test cases
#------
    # int,
    def test_interger_addition(self):
        self.assertEqual(calc_add(7,8), 15)

    # float
    def test_float_addition(self):
        self.assertEqual(calc_add(7.0,8.5), 15.5)

    # int as str
    @unittest.skip("demonstrating skipping")
    def test_int_strings(self):
        self.assertEqual(calc_add("7","8"), 15)

    # float as str
    def test_positive_negative(self):
        self.assertEqual(calc_add(-7,8), 1)


if __name__ == '__main__':
    unittest.main()


#manual testing
#adding own if else stmnts to verify
#in built assert statements
#unittest frameworks