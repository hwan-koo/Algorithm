import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(range(101))
visited = [0] * 101

for _ in range(N):
    x, y = map(int, input().split())
    A[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    A[u] = v


def BFS(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        now = queue.popleft()
        for k in range(1, 7):
            go = now + k
            if go > 100:
                continue
            num = A[go]
            if visited[num] == 0:
                queue.append(num)
                visited[num] = visited[now] + 1

BFS(1)
print(visited[100] - 1)
