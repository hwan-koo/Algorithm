import sys
from queue import PriorityQueue
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
A = [[] for _ in range(V+1)]
D = [sys.maxsize] * (V+1)
D[0] = 0
D[start] = 0
visited = [False] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    A[u].append((v, w))

queue = PriorityQueue()
queue.put((0,start))

while queue.qsize() > 0:
    temp = []
    now = queue.get()
    if visited[now[1]]:
        continue
    visited[now[1]] = True
    for i in A[now[1]]:
        if D[i[0]] > D[now[1]] + i[1]:
            D[i[0]] = D[now[1]] + i[1]
            queue.put((D[i[0]], i[0]))

for i in range(1, V+1):
    if not visited[i]:
        print("INF")
    else:
        print(D[i])