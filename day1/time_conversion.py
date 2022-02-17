import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hours = int(s[0:2])
    minutes = int(s[3:5])
    seconds = int(s[6:8])
    am_or_pm = s[8:10]

    if hours == 12 and am_or_pm.lower() == "am":
        hours -= 12
    
    if hours != 12 and am_or_pm.lower() == "pm":
        hours += 12

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
