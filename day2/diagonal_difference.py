import math
import os
import random
import re
import sys

# Function description
# _diagonalDifference_ takes the following parameter:
# int arr[n][m]: a square array of integers
# Returns
# int: the absolute diagonal difference
# Example:
# The square matrix arr shown below:
# 1 2 3
# 4 5 6
# 9 8 9
# The top-left to bottom-right diagonal sums to 15.
# The bottom-left to top-right diagonal sums to 17.
# The absolute difference between the two is 2.

def diagonalDifference(arr):
    diag1 = 0
    diag2 = 0
    for i in range(len(arr)):
        diag1 += arr[i][i]
        diag2 += arr[len(arr)-1-i][i]

    return abs(diag1-diag2)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
