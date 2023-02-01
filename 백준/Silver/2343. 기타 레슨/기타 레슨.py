N, M = map(int, input().split())
class_list = list(map(int, input().split()))

min_length = 0
max_length = 0

for i in class_list:
    if min_length < i:
        min_length = i
    max_length += i

while min_length <= max_length:
    midi = int((min_length + max_length) /2)
    sum = 0
    count = 0
    for i in range(N):
        if sum + class_list[i] > midi:
            count += 1
            sum = 0
        sum += class_list[i]
    if sum != 0:
        count += 1
    if count > M:
        min_length = midi + 1
    else:
        max_length = midi - 1

print(min_length)


