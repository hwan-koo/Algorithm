from collections import deque
N, K = map(int, input().split())
A = [[-1,0] for _ in range(100001)]
queue = deque()
count = [0] * 100001
def BFS(x):
    global count
    queue.append(x)
    A[x][0] = 0
    A[x][1] = 1
    while queue:
        now = queue.popleft()
        choice = [now - 1, now + 1, now * 2]
        for i in choice:
            if 0 > i or i > 100000:
                continue
            if A[i][0] == -1:
                A[i][0] = A[now][0] + 1
                A[i][1] = A[now][1]
                queue.append(i)
            elif A[i][0] == A[now][0] + 1:
                A[i][1] += A[now][1]

BFS(N)
print(A[K][0])
print(A[K][1])