import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
M = int(input())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0
def DFS(x):
    global count
    visited[x] = True
    for i in A[x]:
        if not visited[i]:
            visited[i] = True
            count += 1
            DFS(i)
DFS(1)
print(count)