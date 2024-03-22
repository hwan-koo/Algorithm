from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[False for _ in range(102)] for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 +1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                else:
                    if graph[i][j] != 0:
                        graph[i][j] = 1                
    dx = [1, 0 , -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append([characterX * 2, characterY * 2, 0])
    while queue:
        now = queue.popleft()
        if now[0] == itemX * 2 and now[1] == itemY * 2:
            return now[2] // 2
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if 0<= x < 102 and 0<= y < 102:
                if not visited[x][y] and graph[x][y] == 1:
                    queue.append([x,y,now[2] + 1])
                    visited[x][y] = True
                
    answer = 0
    return answer