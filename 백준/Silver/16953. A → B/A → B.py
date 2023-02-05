A, B = map(int, input().split())
count = 0
limit = 0
while B > A and limit <= 40:
    if B % 2 == 0:
        B = B // 2
        count += 1
    elif int(str(B)[-1]) == 1:
        B = str(B)[:(len(str(B))-1)]
        B = int(float(B))
        count += 1
    limit += 1

if B == A:
    print(count + 1)
else:
    print(-1)