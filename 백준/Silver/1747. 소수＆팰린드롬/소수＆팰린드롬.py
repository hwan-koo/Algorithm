import math
N = int(input())
A = list(range(10 ** 7 + 1))
A[1] = 0
for i in range(2, int(math.sqrt(10 ** 7)) + 1):
    if A[i] == 0:
        continue
    for j in range(i + i, 10 ** 7 + 1, i):
        A[j] = 0
def palindrome(x):
    temp = list(str(x))
    s = 0
    e = len(temp) - 1
    while s < e:
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True
index = N
while True:
    if A[index] != 0:
        if palindrome(A[index]):
            print(A[index])
            break
    index += 1
