import sys
from queue import PriorityQueue
input = sys.stdin.readline
N = int(input())
M = int(input())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
D = [sys.maxsize] * (N+1)
for _ in range(M):
    s, e, cost = map(int, input().split())
    A[s].append((e, cost))
start, end = map(int, input().split())
queue = PriorityQueue()
queue.put((0, start))
D[start] = 0
D[0] = 0
while queue.qsize() > 0:
    now = queue.get()
    if visited[now[1]]:
        continue
    visited[now[1]] = True
    for i in A[now[1]]:
        if D[i[0]] > D[now[1]] + i[1]:
            D[i[0]] = D[now[1]] + i[1]
            queue.put((D[i[0]], i[0]))
print(D[end])
