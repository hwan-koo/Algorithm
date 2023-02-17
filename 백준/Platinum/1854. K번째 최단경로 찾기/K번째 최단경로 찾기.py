import sys
from queue import PriorityQueue
input = sys.stdin.readline
n, m, k = map(int, input().split())
A = [[] for _ in range(n+1)]
D = [[sys.maxsize] * k for _ in range(n+1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    A[s].append((e, cost))
queue = PriorityQueue()
queue.put((0, 1))
D[1][0] = 0
while queue.qsize() > 0:
    now = queue.get()
    cost = now[0]
    node = now[1]
    for i in A[node]:
        plus_cost = cost + i[1]
        if D[i[0]][k - 1] > plus_cost:
            D[i[0]][k - 1] = plus_cost
            D[i[0]].sort()
            queue.put((plus_cost, i[0]))

for i in range(1, n+1):
    if D[i][k-1] == sys.maxsize:
        print(-1)
        continue
    else:
        print(D[i][k-1])
