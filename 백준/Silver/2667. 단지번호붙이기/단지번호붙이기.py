import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
input = sys.stdin.readline
N = int(input())
A = [[] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
for i in range(N):
    temp = str(input()).rstrip()
    for j in range(N):
        A[i].append(int(temp[j]))
        if int(temp[j]) == 0:
            visited[i][j] = True
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
count_list = []
def DFS(x, y):
    global count_list, count
    visited[x][y] = True
    for k in range(4):
        X = x + dx[k]
        Y = y + dy[k]
        if 0 <= X < N and 0 <= Y < N and not visited[X][Y]:
            DFS(X, Y)
            count += 1

dangi = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dangi += 1
            count = 1
            DFS(i, j)
            count_list.append(count)
print(dangi)
count_list.sort()
for i in count_list:
    print(i)