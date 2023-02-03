import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(input().rstrip())

for _ in range(M):
    B.append(input().rstrip())

A = set(A)
B = set(B)

C = list(A.intersection(B))
C.sort()
print(len(C))
for i in C:
    print(i)