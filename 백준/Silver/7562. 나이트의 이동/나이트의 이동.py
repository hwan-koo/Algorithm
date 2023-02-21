import sys
from collections import deque
input = sys.stdin.readline
T = int(input())


def BFS(x, y):
    if x == goal_x and y == goal_y:
        return
    queue = deque()
    queue.append((x, y))
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    while queue:
        present = queue.popleft()
        for k in range(8):
            X = present[0] + dx[k]
            Y = present[1] + dy[k]
            if 0 <= X < size and 0 <= Y < size:
                if not visited[X][Y]:
                    visited[X][Y] = True
                    chess[X][Y] = chess[present[0]][present[1]] + 1
                    if X == goal_x and Y == goal_y:
                        return
                    else:
                        queue.append((X, Y))


for _ in range(T):
    size = int(input())
    now_x, now_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    chess = [[0] * size for _ in range(size)]
    visited = [[False] * size for _ in range(size)]
    BFS(now_x,now_y)
    print(chess[goal_x][goal_y])