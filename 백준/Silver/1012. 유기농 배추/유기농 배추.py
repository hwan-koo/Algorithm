import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())


def DFS(i, j):
    visited[i][j] = True
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < N and 0 <= y < M:
            if A[x][y] != 0 and not visited[x][y]:
                DFS(x, y)


for _ in range(T):
    M, N, K = map(int, input().split())
    A = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for _ in range(K):
        s, e = map(int, input().split())
        A[e][s] = 1
    count = 0
    for a in range(N):
        for b in range(M):
            if A[a][b] != 0 and not visited[a][b]:
                count += 1
                DFS(a, b)
    print(count)
