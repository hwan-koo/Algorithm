import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
A = []
def DFS(k):
    if len(A) == M:
        print(*A)
        return
    for i in range(k, N):
        A.append(input_list[i])
        DFS(i)
        A.pop()
DFS(0)