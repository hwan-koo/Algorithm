from collections import deque
def solution(maps):
    n = len(maps) # 행
    m = len(maps[0]) # 열
    
    queue = deque()
    queue.append([0,0,1])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    maps[0][0] = 0
    while queue:
        now = queue.popleft()
        for i in range(4):
            x = dx[i] + now[0]
            y = dy[i] + now[1]
            if  0 <= x < n and 0 <= y < m:
                if maps[x][y] != 0:
                    maps[x][y] = 0
                    queue.append([x, y, now[2] + 1])
        if now[0] == n-1 and now[1] == m - 1:
            return now[2]
                
    answer = -1
    return answer