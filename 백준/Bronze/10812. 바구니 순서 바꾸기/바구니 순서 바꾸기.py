N, M = map(int, input().split())
A = list(range(N + 1))
for _ in range(M):
    i, j, k = map(int, input().split())
    A[i:j+1] = A[k:j+1] + A[i: k]
A.pop(0)
print(*A)