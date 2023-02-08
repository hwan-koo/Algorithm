import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
T = int(input())

A = [[0] * 2 for _ in range(41)]
A[0][0] = 1
A[1][1] = 1

for i in range(2, 41):
    A[i][0] = A[i-2][0] + A[i-1][0]
    A[i][1] = A[i-2][1] + A[i-1][1]


for _ in range(T):
    N = int(input())
    print(*A[N])
