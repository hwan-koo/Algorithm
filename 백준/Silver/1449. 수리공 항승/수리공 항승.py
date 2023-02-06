N, L = map(int, input().split())
water_list = list(map(int, input().split()))
A = [0] * 2002

for i in water_list:
    A[2 * i - 1] = 1
    A[2 * i] = 1
    A[2 * i + 1] = 1
index = 1
count = 0
while index <= 2001:
    if A[index] == 1:
        index += 2 * L + 1
        count += 1
    else:
        index += 1
print(count)


