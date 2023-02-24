import math
N = input()
num = [0] * 10
for i in N:
    num[int(i)] += 1
hap = num[6] + num[9]
num[6] = math.ceil(hap /2)
num[9] = math.ceil(hap /2)
print(max(num))