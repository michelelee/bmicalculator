# convert weight in pounds to kg (divide by 2.2)
# convert height from inches to meters
# calculation is weight in kg divided by height in meters


def bmi(height, weight):
	height_meters = height * 0.025
	weight_kg = weight * 0.45

	if height_meters == 0:
		return 0

	return round(weight_kg / height_meters**2, 1)

def test():
	assert bmi(63, 125) == 22.7
	assert bmi(0, 125) == 0

	print('All Test Passed')


if __name__ == '__main__':
	test()