import sys
N = int(input())
sys.setrecursionlimit(10 ** 6)


def factorial(x):
    answer = 1
    if x > 1:
        answer = x * factorial(x-1)
    return answer


print(factorial(N))