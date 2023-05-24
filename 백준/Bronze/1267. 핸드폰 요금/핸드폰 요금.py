n = int(input())
call_list = list(map(int, input().split()))

y = 0
m = 0
for i in call_list:
    y += i // 30 + 1
    m += i // 60 + 1
y = 10 * y
m = 15 * m
if y < m:
    print(f"Y {y}")
elif y > m:
    print(f"M {m}")
else:
    print(f"Y M {m}")