#!/bin/python3

import math
import os
import random
import re
import sys


def reverseArray(arr,size):

    for i in range(size-1,-1,-1):
        print(arr[i], end=' ')
    pass

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    reverseArray(arr,n)