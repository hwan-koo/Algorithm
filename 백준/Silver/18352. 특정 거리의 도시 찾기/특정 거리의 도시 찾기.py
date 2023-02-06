from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
A = [[] for _ in range(N + 1)]
visit_list = [-1] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)


def BFS(x):
    queue = deque()
    queue.append(x)
    visit_list[x] += 1
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if visit_list[i] == -1:
                visit_list[i] = visit_list[now_node] + 1
                queue.append(i)


BFS(X)
answer = []
for i in range(N + 1):
    if visit_list[i] == K:
        answer.append(i)

if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)
