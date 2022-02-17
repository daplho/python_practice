import math
import os
import random
import re
import sys

# Function Description
# lonelyinteger has the following parameter:
# * int a[n]: an array of integers
# Returns:
# * int: the element that occurs only once
# Example:
# a = [1,2,3,4,3,2,1]
# The unique element is 4.

def lonelyinteger(a):
    counts = {}
    for i in a:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1

    for i in counts.keys():
        if counts[i] == 1:
            return i

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)