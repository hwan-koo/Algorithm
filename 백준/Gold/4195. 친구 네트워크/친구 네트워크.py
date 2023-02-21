import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
T = int(input())

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        people[a] += people[b]

for _ in range(T):
    F = int(input())
    people = {}
    parent = {}
    for _ in range(F):
        a, b = map(str, input().split())
        if a not in people:
            parent[a] = a
            people[a] = 1
        if b not in people:
            people[b] = 1
            parent[b] = b
        union(a, b)
        print(people[find(a)])
