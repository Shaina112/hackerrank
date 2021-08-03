#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent

if __name__ == '__main__':

    print('Enter the meal cost in Float: ')
    meal_cost = float(input().strip())


    print('Enter the tip percentage in Integer: ')

    tip_percent = int(input().strip())

    print('Enter the tax percentage in Integer: ')

    tax_percent = int(input().strip())

    tip_amount = meal_cost * tip_percent / 100
    tax_amount = meal_cost * tax_percent / 100
    total_cost = meal_cost + tip_amount + tax_amount

    print(round(total_cost))
