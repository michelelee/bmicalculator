import unittest
from bmi import bmi, body_fat


class TestBMI(unittest.TestCase):

    def test_valid_bmi_input(self):
        self.assertEqual(bmi(63, 125), 22.7)

    def test_should_return_zero_if_height_zero(self):
        "if input height is zero should return zero bmi"
        self.assertEqual(bmi(0, 125), 0, msg='should be 0')


class TestBodyFat(unittest.TestCase):

    def test_valid_male_body_fat_input(self):
        self.assertEqual(body_fat(70, 40, 20), 19.4)

    def test_valid_female_body_fat_input(self):
        self.assertEqual(body_fat(70, 40, 20, 40), 31.8)


if __name__ == '__main__':
    unittest.main()
