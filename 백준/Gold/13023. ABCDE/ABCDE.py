import sys
N, M = map(int, input().split())
sys.setrecursionlimit(10 ** 6)

visited = [False] * N
A = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
end = False


def DFS(now, depth):
    global end
    if depth == 5:
        end = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[now] = False #다른 노드에서 탐색하므로 다시 False값 할당


for i in range(N):
    DFS(i, 1)
    if end:
        break

if end:
    print(1)
else:
    print(0)
