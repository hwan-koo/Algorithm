import math
mi, ma = map(int, input().split())
A = [False] * (ma - mi +1)
for i in range(2, int(math.sqrt(ma) + 1)):
    power = i * i
    index = int(mi / power)
    if mi % power != 0:
        index += 1
    for j in range(index, int(ma/power) + 1):
        A[int((j * power) - mi)] = True
count = 0
for i in A:
    if not i:
        count += 1
print(count)