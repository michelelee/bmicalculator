import unittest
from bmi import bmi


class TestBMI(unittest.TestCase):

    def test_valid_bmi_input(self):
        self.assertEqual(bmi(63, 125), 22.7)

    def test_should_return_zero_if_height_zero(self):
        "if input height is zero should return zero bmi"
        self.assertEqual(bmi(0, 125), 0, msg='should be 0')


if __name__ == '__main__':
    unittest.main()
