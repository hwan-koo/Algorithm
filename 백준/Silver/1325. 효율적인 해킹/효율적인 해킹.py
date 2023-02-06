from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)

visit_list = [False] * (N+1)
confidence_list = [0] * (N+1)


def BFS(x):
    queue = deque()
    queue. append(x)
    visit_list[x] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visit_list[i]:
                visit_list[i] = True
                confidence_list[i] += 1
                queue.append(i)


for i in range(1, N + 1):
    visit_list = [False] * (N+1)
    BFS(i)

ma = 0

for i in range(1, N+1):
    ma = max(ma, confidence_list[i])

for i in range(1, N + 1):
    if confidence_list[i] == ma:
        print(i, end=" ")