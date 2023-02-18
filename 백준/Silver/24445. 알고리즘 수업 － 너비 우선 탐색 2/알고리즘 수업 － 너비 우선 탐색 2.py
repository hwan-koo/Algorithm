import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

index = 1
answer[R] = index
queue = deque()
queue.append(R)
def BFS(s):
    global index
    visited[s] = True
    while queue:
        now = queue.popleft()
        A[now].sort(reverse=True)
        for i in A[now]:
            if not visited[i]:
                queue.append(i)
                index += 1
                visited[i] = True
                answer[i] = index
BFS(R)
answer.pop(0)
for i in answer:
    print(i)