import sys
N = int(input())
sys.setrecursionlimit(10 ** 6)


def star(x):
    if x == 1:
        return ["*"]
    figure = star(x//3)
    A = []

    for X in figure:
        A.append(X * 3)
    for X in figure:
        A.append(X + " " * (x//3) + X)
    for X in figure:
        A.append(X * 3)
    return A


print("\n".join(star(N)))
