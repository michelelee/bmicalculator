# convert weight in pounds to kg (divide by 2.2)
# convert height from inches to meters
# calculation is weight in kg divided by height in meters
# % body fat = 86.010 x log10(abdomen - neck) - 70.041 x log10(height) + 36.76
# % body fat = 163.205 x log10(waist + hip - neck) - 97.684 x log10(height) - 78.387

import math


def bmi(height, weight):
    height_meters = height * 0.025
    weight_kg = weight * 0.45

    if height_meters == 0:
        return 0

    return round(weight_kg / height_meters**2, 1)


def body_fat(height, abdomen, neck, hip=None):
    if hip is None:
        return round(86.010 * math.log10(abdomen - neck) - 70.041 * math.log10(height) + 36.76, 1)
    else:
        return round((163.205 * math.log10(abdomen + hip - neck)) - (97.684 * math.log10(height)) - 78.387, 1)


def test_bmi():
    assert bmi(63, 125) == 22.7
    assert bmi(0, 125) == 0

    print('BMI Test Passed')


def test_body_fat():
    assert body_fat(70, 40, 20) == 19.4
    assert body_fat(70, 40, 20, 40) == 31.6

    print('Body Fat Test Passed')


if __name__ == '__main__':
    test_bmi()
    test_body_fat()