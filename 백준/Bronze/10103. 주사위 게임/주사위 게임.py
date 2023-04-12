n = int(input())
x = 100
y = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        continue
    elif a < b:
        x -= b
    else:
        y -= a
print(x)
print(y)