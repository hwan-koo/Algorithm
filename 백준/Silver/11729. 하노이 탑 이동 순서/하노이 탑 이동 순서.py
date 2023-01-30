import sys
N = int(input())
sys.setrecursionlimit(10 ** 6)


def hanoi(x, s, e):
    if x == 1:
        print(s, e)
        return
    hanoi(x-1, s, 6-s-e)
    print(s, e)
    hanoi(x-1, 6 - s - e, e)


print(2**N-1)
hanoi(N, 1, 3)