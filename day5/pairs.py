#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    pairs = 0
    arr.sort()
    if len(arr) <= 1:
        return 0

    for i in range(len(arr)):
        if i+1 >= len(arr):
            break
        for j in arr[i+1:]:
            if abs(arr[i]-j) == k:
                pairs += 1
                break
    return pairs

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)