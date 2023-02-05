N, K = map(int, input().split())
top = N
bottom = 1
if K == 0 or K == N:
    print(1)
else:
    for i in range(1, K):
        top = top * (N - i)
    for i in range(1, K +1):
        bottom = bottom * i

    print(int(top/bottom))