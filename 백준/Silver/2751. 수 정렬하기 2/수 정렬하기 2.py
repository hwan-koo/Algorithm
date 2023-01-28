import sys
input = sys.stdin.readline

N = int(input())
A = []

for _ in range(N):
  A.append(int(input()))
A.sort()

for i in A:
  print(i)