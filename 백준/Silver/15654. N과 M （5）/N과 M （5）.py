import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
A = []
def DFS():
    if len(A) == M:
        print(*A)
        return
    for i in range(N):
        if input_list[i] in A:
            continue
        A.append(input_list[i])
        DFS()
        A.pop()
DFS()