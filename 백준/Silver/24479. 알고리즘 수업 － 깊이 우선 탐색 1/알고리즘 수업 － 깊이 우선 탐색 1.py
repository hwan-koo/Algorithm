import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M, R = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)
for _ in range(M):
    u, v = map(int ,input().split())
    A[u].append(v)
    A[v].append(u)

index = 1
answer[R] = index
def DFS(s):
    global index
    index += 1
    visited[s] = True
    A[s].sort()
    for i in A[s]:
        if not visited[i]:
            answer[i] = index
            DFS(i)
DFS(R)
answer.pop(0)
for i in answer:
    print(i)