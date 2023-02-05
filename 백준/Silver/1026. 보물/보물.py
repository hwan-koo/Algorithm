N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
sum = 0
for i in range(N):
    sum += A[i] * B[N- i -1]

print(sum)