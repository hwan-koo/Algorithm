from collections import deque
def solution(maps):
    answer = 0
    queue = deque()
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    def BFS(x,y):
        queue.append((x,y))
        visited[x][y] = True
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while queue:
            now = queue.popleft()
            for k in range(4):
                X = now[0] + dx[k]
                Y = now[1] + dy[k]
                if 0 <= X < len(maps) and 0 <= Y < len(maps[0]):
                    if not visited[X][Y]:
                        if maps[X][Y] == 0:
                            visited[X][Y] = True
                        else:
                            maps[X][Y] = maps[now[0]][now[1]] + 1
                            visited[X][Y] = True
                            queue.append((X,Y))
    BFS(0,0)
    answer = maps[len(maps)-1][len(maps[0])-1]
    print(answer)
    if answer == 1:
        answer = -1
    return answer