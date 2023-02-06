import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    P = []
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        P.append((a, b))
    P.sort()
    A = P[0]
    count = 1
    for i in range(1, N):
        if P[i][1] < A[1]:
            A = P[i]
            count += 1
    print(count)