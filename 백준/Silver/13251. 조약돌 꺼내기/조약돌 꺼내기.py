M = int(input())
stone = list(map(int, input().split()))
K = int(input())
N = sum(stone)
D = [[0] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    D[i][i] = 1
    D[i][1] = i
    D[i][0] = 1
for i in range(2,N+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]
top = 0
bottom = D[N][K]
for i in stone:
    if i < K:
        continue
    else:
        top += D[i][K]
print(top / bottom)