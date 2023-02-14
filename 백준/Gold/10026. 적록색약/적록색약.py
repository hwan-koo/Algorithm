import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
A = []
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    A.append(list(map(str, input()))[:N])


def DFS(i, j):
    visited[i][j] = True
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < N and 0 <= y < N:
            if A[i][j] == A[x][y] and not visited[x][y]:
                DFS(x, y)

count1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count1 += 1
            DFS(i, j)
print(count1,end=" ")

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] == "G":
            A[i][j] = "R"
count2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count2 += 1
            DFS(i, j)
print(count2)