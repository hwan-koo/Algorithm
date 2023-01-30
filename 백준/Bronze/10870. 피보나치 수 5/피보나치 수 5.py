import sys
n = int(input())
sys.setrecursionlimit(10 ** 6)


def pivonachi(x):
    answer = 1
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x > 1:
        answer = pivonachi(x - 1) + pivonachi(x - 2)
    return answer


print(pivonachi(n))