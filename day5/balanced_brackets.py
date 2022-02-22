import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    brackets = []
    for c in s:
        if c == '{' or c == '[' or c == '(':
            brackets.append(c)
        elif c == '}':
            try:
                match = brackets.pop()
                if match != '{':
                    return "NO"
            except IndexError:
                return "NO"
        elif c == ']':
            try:
                match = brackets.pop()
                if match != '[':
                    return "NO"
            except IndexError:
                return "NO"
        elif c == ')':
            try:
                match = brackets.pop()
                if match != '(':
                    return "NO"
            except IndexError:
                return "NO"

    if len(brackets) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)