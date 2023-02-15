from collections import deque
N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
D = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    D[b] += 1

queue = deque()

for i in range(1, N+1):
    if D[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end=" ")
    for i in A[now]:
        D[i] -= 1
        if D[i] == 0:
            queue.append(i)

