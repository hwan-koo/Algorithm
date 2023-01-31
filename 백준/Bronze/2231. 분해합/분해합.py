N = int(input())

A = [0] * 1000054

def constructor(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    sum += x
    return sum


for i in range(1,1000001):
    if constructor(i) == N:
        print(i)
        break
    if i == 1000000:
        print(0)