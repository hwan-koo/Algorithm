N = int(input())
D = [0] * 1000001
D[1] = 1
D[2] = 2
for i in range(3, N+1):
    D[i] = (D[i-1] + D[i-2]) % 15746
print(D[N])