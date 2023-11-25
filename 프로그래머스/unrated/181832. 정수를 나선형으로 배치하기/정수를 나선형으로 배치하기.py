def solution(n):
    if n == 1:
        return [[1]]
    answer = [[0] * (n) for _ in range(n)]
    a = 0
    b = 0
    dir = "r"
    for i in range(n * n):
        answer[a][b] = i + 1
        if dir == "r":
            b += 1
            if b == n -1 or answer[a][b+1] != 0:
                dir = "d"
        elif dir == "d":
            a += 1
            if a == n - 1 or answer[a+1][b] != 0:
                dir = "l"
        elif dir == "l":
            b -= 1
            if b == 0 or answer[a][b-1] != 0:
                dir = "u"
        elif dir == "u":
            a -= 1
            if a == 0 or answer[a-1][b] != 0:
                dir = "r"
                
            
    
    
    return answer