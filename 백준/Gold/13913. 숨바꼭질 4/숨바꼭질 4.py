from collections import deque
N, K = map(int, input().split())
A = [-1] * 100001
visited = [-1] * 100001
queue = deque()
path = []
def BFS(x):
    queue.append(x)
    A[x] = 0
    visited[x] = x
    while queue:
        now = queue.popleft()
        if now == K:
            index = now
            while index != N:
                path.append(index)
                index = visited[index]
            path.append(N)
            return A[K]
        choice = [now - 1, now + 1, now * 2]
        for i in choice:
            if 0 > i or i > 100000:
                continue
            if A[i] == -1:
                A[i] = A[now] + 1
                visited[i] = now
                queue.append(i)

print(BFS(N))
print(*path[::-1])
