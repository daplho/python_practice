import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    sorted_grid = []
    for i in range(len(grid)):
        str = grid[i]
        sorted_str = ''.join(sorted(str))
        sorted_grid.append(sorted_str)

    column = 0
    row = 0
    while column < len(sorted_grid[0]):
        cursor = 'a'
        while row < len(sorted_grid):
            if cursor > sorted_grid[row][column]:
                return "NO"
            cursor = sorted_grid[row][column]
            row += 1
        row = 0
        column += 1
    return "YES"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)