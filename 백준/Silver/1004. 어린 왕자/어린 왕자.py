import math
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        distance1 = math.sqrt((x1 - cx) * (x1 - cx) + (y1 - cy) * (y1 - cy))
        distance2 = math.sqrt((x2 - cx) * (x2 - cx) + (y2 - cy) * (y2 - cy))
        if distance1 < r and distance2 < r:
            continue
        elif distance1 < r:
            count += 1
        elif distance2 < r:
            count += 1
    print(count)
