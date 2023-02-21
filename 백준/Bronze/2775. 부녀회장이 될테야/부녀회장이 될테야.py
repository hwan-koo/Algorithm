T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    hb = [[0 for _ in range(n)] for _ in range(k+1)]
    for a in range(n):
        hb[0][a] = a + 1
    for i in range(1, k+1):
        for j in range(n):
            hb[i][j] = sum(hb[i-1][0:j+1])
    print(hb[k][n-1])