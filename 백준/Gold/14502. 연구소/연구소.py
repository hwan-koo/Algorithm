import copy
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
A = []
candidate = []
for _ in range(N):
    A.append(list(map(int ,input().split())))
for i in range(N):
    for j in range(M):
        if A[i][j] == 0:
            candidate.append((i,j))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
queue = deque()
visited = [[False] * M for _ in range(N)]
def BFS(x,y):
    queue.append((x,y))
    while queue:
        now = queue.popleft()
        if B[now[0]][now[1]] == 2:
            for k in range(4):
                X = now[0] + dx[k]
                Y = now[1] + dy[k]
                if 0 <= X < N and 0 <= Y < M:
                    if not visited[X][Y]:
                        if B[X][Y] == 0:
                            B[X][Y] = 2
                            visited[X][Y] = True
                            queue.append((X,Y))


B = copy.deepcopy(A)
visited = [[False] * M for _ in range(N)]
wall = []
answer = []
for i in range(len(candidate) - 2):
    for j in range(i+1, len(candidate) - 1):
        for k in range(j+1, len(candidate)):
            B[candidate[i][0]][candidate[i][1]] = 1
            B[candidate[j][0]][candidate[j][1]] = 1
            B[candidate[k][0]][candidate[k][1]] = 1
            for a in range(N):
                for b in range(M):
                    BFS(a, b)
            count = 0
            for x in range(N):
                count += B[x].count(0)
            answer.append(count)
            B = copy.deepcopy(A)
            visited = [[False] * M for _ in range(N)]

print(max(answer))