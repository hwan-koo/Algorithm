import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = []
answer = []
for _ in range(N):
    A.append(list(map(int, input().split())))


def BFS(a, b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        now = queue.popleft()
        for t in range(4):
            X = now[0] + dx[t]
            Y = now[1] + dy[t]
            if 0 <= X < N and 0 <= Y < N:
                if not visited[X][Y]:
                    visited[X][Y] = True
                    queue.append((X,Y))


high = 0
for i in A:
    if max(i) > high:
        high = max(i)

for i in range(1, high):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for a in range(N):
        for b in range(N):
            if A[a][b] <= i:
                visited[a][b] = True
    for j in range(N):
        for k in range(N):
            if not visited[j][k]:
                BFS(j, k)
                count += 1
    answer.append(count)
if answer:
    print(max(answer))
else:
    print(1)



