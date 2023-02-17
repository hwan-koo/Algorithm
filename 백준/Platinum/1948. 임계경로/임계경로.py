import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())
A = [[] for _ in range(N+1)]
A_reverse = [[] for _ in range(N+1)]
D = [0] * (N+1)

for i in range(M):
    s, e, time = map(int, input().split())
    A[s].append((e,time))
    A_reverse[e].append((s,time))
    D[e] += 1
start, end = map(int, input().split())
queue = deque()
queue.append(start)
result = [0] * (N+1)

while queue:
    now = queue.popleft()
    for i in A[now]:
        D[i[0]] -= 1
        result[i[0]] = max(result[i[0]], result[now] + i[1])
        if D[i[0]] == 0:
            queue.append(i[0])

count = 0
visited = [False] * (N+1)
queue.clear()
queue.append(end)
visited[end] = True

while queue:
    now = queue.popleft()
    for i in A_reverse[now]:
        if result[i[0]] + i[1] == result[now]:
            count += 1
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
print(result[end])
print(count)