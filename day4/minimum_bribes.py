import math
import os
import random
import re
import sys

def find_smaller(n, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] < n:
            count += 1
    return count

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    total_bribes = 0
    for i in range(len(q)):
        bribes = find_smaller(q[i], q[i+1:])
        if bribes > 2:
            print("Too chaotic")
            return
        else:
            total_bribes += bribes

    print(total_bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)