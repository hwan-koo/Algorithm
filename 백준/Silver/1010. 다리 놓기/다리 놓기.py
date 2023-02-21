import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    D = [[0] * (M+1) for _ in range(M+1)]
    for i in range(M+1):
        D[i][i] = 1
        D[i][1] = i
        D[i][0] = 1
    for i in range(2, M+1):
        for j in range(1, i):
            D[i][j] = D[i-1][j] + D[i-1][j-1]
    print(D[M][N])