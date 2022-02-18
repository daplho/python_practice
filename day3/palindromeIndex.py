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
    if isPalindrome(s):
        return -1

    for i in range(len(s)):
        testString = s[0:i]+s[i+1:]
        if isPalindrome(testString):
            return i
    return -1

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)
