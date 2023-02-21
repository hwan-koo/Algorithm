N = int(input())
M = int(input())
if M != 0:
    broken = list(map(int, input().split()))
else:
    broken = []
now = 100
count = abs(now - N)

for i in range(1000001):
    for j in str(i):
        if int(j) in broken:
            break
    else:
        count = min(count, len(str(i)) + abs(i - N))
print(count)