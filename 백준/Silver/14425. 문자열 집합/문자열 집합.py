N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(input())

A = set(A)
count = 0
for _ in range(M):
    if input() in A:
        count += 1
print(count)