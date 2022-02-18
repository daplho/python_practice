#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isPalindrome(s):
    reversed = s[::-1]

    return s == reversed

def palindromeIndex(s):
    if len(s) == 1:
        return -1
    if len(s) == 2:
        return 0

    i = 0
    j = len(s) - 1
    p = -1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        else:
            if p == -1 and i+1 < j and s[i+1] == s[j]:
                p = i
                i += 1
                continue
            elif p == -1 and i < j-1 and s[i] == s[j-1]:
                p = j
                j -=1
                continue
            else:
                if i == j:
                    return -1
                elif j - i == 1 and s[i] != s[j]:
                    return i
                else:
                    return -1
    return p

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)
