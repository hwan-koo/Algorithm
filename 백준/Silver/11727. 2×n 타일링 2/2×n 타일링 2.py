N = int(input())

D = [0] * 1001
D[1] = 1
D[2] = 3
D[3] = 5
for i in range(4, N+1):
    D[i] = D[i-1] + 2 * D[i-2]
print(D[N] % 10007)