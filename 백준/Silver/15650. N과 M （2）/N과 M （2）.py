import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
A = []
def DFS(k):
    if len(A) == M:
        print(*A)
        return
    for i in range(k, N+1):
        if i not in A:
            A.append(i)
            DFS(i)
            A.pop()
DFS(1)
