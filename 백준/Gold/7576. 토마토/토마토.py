import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
A = [[0] * M for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
start = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    tomato = list(map(int,input().split()))
    for j in range(M):
        A[i][j] = tomato[j]
        if tomato[j] == -1:
            visited[i][j] = True
        if tomato[j] == 1:
            start.append((i,j))

def BFS(a):
    queue = deque()
    for t in a:
        queue.append(t)
        visited[t[0]][t[1]] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[1] + dx[k]
            y = now[0] + dy[k]
            if 0 <= x < M and 0 <= y < N:
                if not visited[y][x]:
                    visited[y][x] = True
                    A[y][x] = A[now[0]][now[1]] + 1
                    queue.append((y, x))


BFS(start)

ma = []
answer = True
for i in range(N):
    if 0 in A[i]:
        answer = False
        break
    ma.append(max(A[i]))
if answer:
    print(max(ma)-1)
else:
    print(-1)