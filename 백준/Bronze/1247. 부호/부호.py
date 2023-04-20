import sys
input = sys.stdin.readline
for _ in range(3):
    N = int(input())
    count = 0
    for _ in range(N):
        a = int(input())
        count += a
    if count > 0:
        print("+")
    elif count < 0:
        print("-")
    else:
        print(0)
    