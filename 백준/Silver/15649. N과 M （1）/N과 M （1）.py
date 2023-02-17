import sys

sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
A = []
def DFS():
    if len(A) == M:
        print(*A)
        return
    for i in range(1, N+1):
        if i not in A:
            A.append(i)
            DFS()
            A.pop()

DFS()
