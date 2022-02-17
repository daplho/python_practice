import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for num in arr:
        if num > 0:
            positive += 1
        elif num == 0:
            zero += 1
        else:
            negative +=1

    print("{0:.6f}".format(positive/len(arr)))
    print("{0:.6f}".format(negative/len(arr)))
    print("{0:.6f}".format(zero/len(arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)