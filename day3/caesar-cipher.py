import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    encoded = ""
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            new_int_representation = ord('A') + (ord(s[i]) - ord('A')+k) % 26
            encoded += chr(new_int_representation)
        elif 'a' <= s[i] <= 'z':
            new_int_representation = ord('a') + (ord(s[i]) - ord('a')+k) % 26
            encoded += chr(new_int_representation)
        else:
            encoded += s[i]
    return encoded

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
