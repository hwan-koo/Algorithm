import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    x, y = map(int, input().split())
    A.append((x,y))
A.sort(key=lambda x:x[1])
A.sort()
for i in A:
    print(i[0], i[1])