X = int(input())
A = [0] * (X + 1)

for i in range(2, X+1):
    A[i] = A[i - 1] + 1
    if i % 3 == 0:
        A[i] = min(A[i], A[i // 3] + 1)
    if i % 2 == 0:
        A[i] = min(A[i], A[i // 2] + 1)

print(A[X])