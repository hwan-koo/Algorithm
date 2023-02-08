import math
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    #한쪽 원이 한쪽 원안에 있는 경우
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    if distance + min(r1,r2) < max(r1,r2):
        print(0)
        continue
    elif distance + min(r1,r2) == max(r1,r2):
        print(1)
        continue
    elif distance + min(r1,r2) > max(r1,r2):
        if distance == r1 + r2:
            print(1)
            continue
        elif distance > r1 + r2:
            print(0)
            continue
        elif distance < r1 + r2:
            print(2)
            continue
