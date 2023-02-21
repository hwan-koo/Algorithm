import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
A = [[[0] * M for _ in range(N)] for _ in range(H)]
dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]
start = []
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
for k in range(H):
    for i in range(N):
        tomato = list(map(int,input().split()))
        for j in range(M):
            A[k][i][j] = tomato[j]
            if tomato[j] == -1:
                visited[k][i][j] = True
            if tomato[j] == 1:
                start.append((i,j,k))
def BFS(a):
    queue = deque()
    for t in a:
        queue.append(t)
        visited[t[2]][t[0]][t[1]] = True
    while queue:
        now = queue.popleft()
        for k in range(6):
            x = now[1] + dx[k]
            y = now[0] + dy[k]
            z = now[2] + dz[k]
            if 0 <= x < M and 0 <= y < N and 0 <= z < H:
                if not visited[z][y][x]:
                    visited[z][y][x] = True
                    A[z][y][x] = A[now[2]][now[0]][now[1]] + 1
                    queue.append((y, x, z))
go = False
for i in range(H):
    for j in range(N):
        if 0 in A[i][j]:
            go = True
            break
if go:
    BFS(start)
    ma = []
    answer = True
    for i in range(H):
        for j in range(N):
            if 0 in A[i][j]:
                answer = False
                break
            ma.append(max(A[i][j]))
    if answer:
        print(max(ma)-1)
    else:
        print(-1)
else:
    print(0)