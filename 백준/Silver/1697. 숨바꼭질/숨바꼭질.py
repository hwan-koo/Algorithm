from collections import deque
N, K = map(int, input().split())
A = [0] * 100001
visited = [False] * 100001
queue = deque()
def BFS(x):
    queue.append(x)
    visited[x] = True
    while queue:
        now = queue.popleft()
        choice = [now - 1, now + 1, now * 2]
        for i in choice:
            if 0 > i or i > 100000:
                continue
            if not visited[i]:
                visited[i] = True
                A[i] = A[now] + 1
                queue.append(i)

BFS(N)
print(A[K])