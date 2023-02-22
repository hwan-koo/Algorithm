import math
a, B = map(int, input().split())
A = list(range(10 ** 7 + 1))
A[1] = 0
for i in range(2, int(math.sqrt(10 ** 7)) + 1):
    if A[i] == 0:
        continue
    for j in range(i + i, 10 ** 7 + 1, i):
        A[j] = 0
count = 0
for i in range(2, 10 ** 7 + 1):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= B / temp:
            if A[i] >= a / temp:
                count += 1
            temp = temp * A[i]
print(count)