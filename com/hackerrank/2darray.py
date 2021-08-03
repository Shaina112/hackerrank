#!/bin/python3

import math
import os
import random
import re
import sys


def findMax(input):
    # find the max value and print it
    max_value = -999
    for i in range(4):
        for j in range(4):
            sum = input[0 + i][0 + j] + input[0 + i][1 + j] + input[0 + i][2 + j] + input[1 + i][1 + j] + input[2 + i][
                0 + j] + input[2 + i][1 + j] + input[2 + i][2 + j]
            if sum > max_value:
                max_value = sum
    print(max_value)


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    findMax(arr)
