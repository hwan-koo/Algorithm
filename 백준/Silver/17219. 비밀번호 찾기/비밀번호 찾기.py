import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = {}
for _ in range(N):
    site, password = map(str,input().split())
    A[site] = password
for _ in range(M):
    find = str(input()).rstrip()
    print(A[find])