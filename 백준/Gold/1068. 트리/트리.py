import sys
sys.setrecursionlimit(10 **  6)
input = sys.stdin.readline
N = int(input())
parent = list(map(int, input().split()))
A = [[] for _ in range(N)]
visited = [False] * N
trash = int(input())
start = parent.index(-1)

for i in range(N):
    if parent[i] == -1:
        continue
    A[parent[i]].append(i)
    A[i].append(parent[i])

answer = 0
def DFS(x):
    global answer
    child = 0
    visited[x] = True
    for i in A[x]:
        if not visited[i] and i != trash:
            child += 1 
            DFS(i)
    if child == 0:
        answer += 1
if trash == start:
    print(0)
else:
    DFS(start)
    print(answer)
            
        