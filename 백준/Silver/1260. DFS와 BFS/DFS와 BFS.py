from collections import deque

N, M, start = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N + 1):
    A[i].sort()


def DFS(v):
    print(v, end=" ")
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


visited = [False] * (N + 1)
DFS(start)


def BFS(v):
    myque = deque()
    visited[v] = True
    myque.append(v)
    while myque:
        present_node = myque.popleft()
        print(present_node, end=" ")
        for i in A[present_node]:
            if not visited[i]:
                visited[i] = True
                myque.append(i)


visited = [False] * (N + 1)
print()
BFS(start)