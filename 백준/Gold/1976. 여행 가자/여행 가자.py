import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
M = int(input())
city = [[0] * (N+1) for _ in range(N+1)]
parent = list(range(N+1))
for i in range(1, N+1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)
tour = list(map(int, input().split()))
tour.insert(0,0)


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


for i in range(1, N+1):
    for j in range(1, N+1):
        if city[i][j] == 1:
            union(i, j)


answer = True
for i in range(2, len(tour)):
    if find(tour[1]) != find(tour[i]):
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")