import sys
T = int(input())
sys.setrecursionlimit(10 ** 6)


def recursion(x, a, b):
    global count
    if a >= b:
        return 1
    elif x[a] != x[b]:
        return 0
    else:
        count += 1
        return recursion(x, a+1, b-1)


def isPalindrome(x):
    return recursion(x, 0, len(x)-1)


for _ in range(T):
    test = str(input())
    count = 1
    print(isPalindrome(test), count)