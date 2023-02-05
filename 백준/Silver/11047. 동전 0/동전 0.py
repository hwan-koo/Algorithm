import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
count = 0
index = N - 1
while K != 0:
    if A[index] <= K:
        count += K // A[index]
        K = K % A[index]
    index -= 1

print(count)
