#!/usr/bin/env python
# convert weight in pounds to kg (divide by 2.2)
# convert height from inches to meters
# calculation is weight in kg divided by height in meters
# % body fat = 86.010 x log10(abdomen - neck) - 70.041 x log10(height) + 36.76
# % body fat = 163.205 x log10(waist + hip - neck) - 97.684 x log10(height) - 78.387

import math
import argparse
import sys


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Fitness Calculator")
    parser.add_argument("--type", "-t",
        choices=['bmi', 'body_fat'],
        help="type of fitness calculation",
        required=True)
    parser.add_argument("--height", "-hgt",
        type=float,
        help="your height in inches")
    parser.add_argument("--weight", "-wgt",
        type=float,
        help="your weight in lbs")
    parser.add_argument("--abdomen", "-abd",
        type=float,
        help="your abdomen circumference in inches")
    parser.add_argument("--neck", "-nk",
        type=float,
        help="your neck circumference in inches")
    parser.add_argument("--hip",
        type=float,
        help="your hip circumference in inches")
    args = parser.parse_args()
    if args.type == "bmi":
        if not hasattr(args, "height"):
            print("height is required for bmi")
            sys.exit(1)
        if not hasattr(args, "weight"):
            print("weight is required for bmi")
            sys.exit(1)
        print(bmi(args.height, args.weight))
    if args.type == "body_fat":
        if not hasattr(args, "height"):
            print("height is required for body_fat")
            sys.exit(1)
        if not hasattr(args, "abdomen"):
            print("abdomen is required for bmi")
            sys.exit(1)()
        if not hasattr(args, "neck"):
            print("neck is required for bmi")
            sys.exit(1)
        import ipdb; ipdb.set_trace()
        if hasattr(args, "hip") and args.hip != None:
            print(body_fat(args.height, args.abdomen, args.neck, args.hip))
        else:
            print(body_fat(args.height, args.abdomen, args.neck))




