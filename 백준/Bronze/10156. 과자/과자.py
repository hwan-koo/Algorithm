K, N, M = map(int, input().split())

required = K * N
if required <= M:
    print(0)
else:
    print(required - M)