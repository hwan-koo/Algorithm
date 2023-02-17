import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
A =[[] for _ in range(N+1)]
visited = [False] * (N+1)
visited[0] = True
answer = [0] * (N+1)
for _ in range(N-1):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


def DFS(x):
    visited[x] = True
    for i in A[x]:
        if not visited[i]:
            visited[x] = True
            answer[i] = x
            DFS(i)


DFS(1)
for i in range(2,N+1):
    print(answer[i])