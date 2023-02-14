import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
parent = list(range(N+1))


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


def set_check(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False


for i in range(M):
    order, a, b = map(int, input().split())
    if order == 0:
        union(a,b)
    else:
        if set_check(a,b):
            print("YES")
        else:
            print("NO")