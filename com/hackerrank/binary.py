#!/bin/python3

import math
import os
import random
import re
import sys


def convert_to_binary(n):
    binary_num_arr = []
    while n > 1:
        remainder = n % 2
        n = n // 2
        binary_num_arr.append(remainder)
    if n == 1:
        binary_num_arr.append(1)

    binary_num_arr.reverse()
    return binary_num_arr


def count_ones(arr):
    max_count = 0
    count = 0
    for i in arr:
        if i == 1:
            count += 1
            if count > max_count:
                max_count = count
        if i == 0:
            count = 0
    return max_count


if __name__ == '__main__':
    n = int(input().strip())

    # Step 1, this returns a binary number array of integers
    binary_num = convert_to_binary(n)
    max_count = count_ones(binary_num)

    print(max_count)

    # for num in binary_num:
    # print(binary_num, end=' ')