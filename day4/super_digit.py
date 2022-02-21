import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigitHelper(num):
    if num < 10:
        return num
    
    sum = 0
    remainder = num % 10
    num = num // 10
    while num > 0:
        sum += remainder
        remainder = num % 10
        num = num // 10
    sum += remainder
    return superDigitHelper(sum)

def superDigit(n, k):
    return superDigitHelper(superDigitHelper(int(n)) * k)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)
