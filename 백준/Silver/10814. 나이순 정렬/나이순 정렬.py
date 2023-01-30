import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    age, name = map(str, input().split())
    A.append((int(age), name, i))
A.sort(key=lambda x:(x[0],x[2]))

for j in A:
    print(j[0],j[1])