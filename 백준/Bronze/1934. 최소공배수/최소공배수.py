import sys
input = sys.stdin.readline
def yaksu(a, b):
    if b == 0:
        return a
    else:
        return yaksu(b, a % b)
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    gongbasu = a * b // yaksu(a,b)
    print(gongbasu)