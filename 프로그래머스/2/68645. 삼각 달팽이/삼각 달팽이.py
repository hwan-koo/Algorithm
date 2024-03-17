def solution(n):
    array = [[0] * i for i in range(1, n+1)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    angle = 0
    x = 0
    y = 0
    num = 1
    size = (n * (n+1)) // 2
    while num <= size:
        array[x][y] = num
        nx = x + dx[angle]
        ny = y + dy[angle]
        num += 1
        if 0<= nx < n and 0<= ny <= nx and array[nx][ny] == 0:
            x, y = nx, ny
        else:
            angle =( angle + 1) % 3
            x += dx[angle]
            y += dy[angle]
    answer = []
    for i in array:
        for j in i:
            answer.append(j)
    return answer