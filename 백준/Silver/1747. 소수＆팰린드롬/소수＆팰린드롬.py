import math
N = int(input())
A = list(range(10 ** 7 + 1))
A[1] = 0
for i in range(2, int(math.sqrt(10 ** 7)) + 1):
    if A[i] == 0:
        continue
    for j in range(i + i, 10 ** 7 + 1, i):
        A[j] = 0
for i in range(N, 10 ** 7 + 1):
    if A[i] != 0:
        if "".join(reversed(list(str(A[i])))) == str(A[i]):
            print(A[i])
            break
