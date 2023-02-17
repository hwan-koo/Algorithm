import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = [[] for _ in range(N+1)]
time_list = [0] * (N+1)
D = [0] * (N+1)
for i in range(1, N+1):
    info = list(map(int, input().split()))
    time_list[i] = info[0]
    info.pop(0)
    for j in info:
        if j == -1:
            break
        else:
            A[j].append(i)
            D[i] += 1

queue = deque()
answer = [0] * (N+1)
for i in range(1, N+1):
    if D[i] == 0:
        queue.append(i)
while queue:
    now = queue.popleft()
    for i in A[now]:
        D[i] -= 1
        answer[i] = max(answer[i],answer[now] + time_list[now])
        if D[i] == 0:
            queue.append(i)

for i in range(1, N+1):
    answer[i] += time_list[i]
    print(answer[i])