from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    A = [[-1] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]
    queue = deque()
    for i in rectangle:
        x1 = i[0] * 2
        y1 = i[1] * 2
        x2 = i[2] * 2
        y2 = i[3] * 2
        for a in range(x1, x2 + 1):
            for b in range(y1, y2 + 1):
                if x1 < a < x2 and y1 < b < y2:
                    A[a][b] = 0
                elif A[a][b] != 0:
                    A[a][b] = 1
    
    
    def BFS(u, v):
        queue.append((u * 2, v * 2))
        visited[u * 2][v * 2] = True
        while queue:
            now = queue.popleft()
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for k in range(4):
                X = now[0] + dx[k]
                Y = now[1] + dy[k]
                if 0 <= X < 102 and 0 <= Y < 102:
                    if not visited[X][Y] and A[X][Y] > 0:
                        A[X][Y] = A[now[0]][now[1]] + 1
                        visited[X][Y] = True
                        queue.append((X,Y))
                        
    BFS(characterX,characterY)
    answer = A[itemX * 2][itemY * 2] // 2
    return answer