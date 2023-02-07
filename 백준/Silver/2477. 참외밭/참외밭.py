K = int(input())
A = []
B = []
C = [0] * 5
width = 0
height = 0
width_i = 0
height_i = 0
for i in range(6):
    direction, value = map(int, input().split())
    if direction == 1 or direction == 2:
        if width < value:
            width = value
            width_i = i
    else:
        if height < value:
            height = value
            height_i = i
    A.append(direction)
    B.append(value)


ma = max(width_i,height_i)
mi = min(width_i,height_i)
if ma == 5 and mi == 0:
    ma = 0
sum = B[(ma + 2) % 6] * B[(ma + 3) % 6]

print((height * width - sum) * K)