import math
import os
import random
import re
import sys


def can_we_circumnavigate(start, petrolpumps):
    count = 0
    cur_gas = 0
    while count < len(petrolpumps):
        cur_stop = (start+count) % len(petrolpumps)
        cur_gas += petrolpumps[cur_stop][0]
        cur_gas -= petrolpumps[cur_stop][1]
        if cur_gas <= 0:
            return False
        count += 1

    return True

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    gas = 0
    for i in range(len(petrolpumps)):
        if can_we_circumnavigate(i, petrolpumps):
            return i

    return -1

if __name__ == '__main__':
    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)
    print(result)