def check(x,y, item):
    # 두 칸 밑이 사람인데, 중간에 칸막이가 없는 경우
    if x + 2 <= 4:
        if item[x + 2][y] == "P" and item[x + 1][y] == "O":
            return 0
    # 한 칸 밑에 사람이 있는 경우
    if x + 1 <= 4 :
        if item[x + 1][y] == "P":
            return 0
    # 두 칸 오른쪽에 사람이 있는데 칸막이가 없는 경우
    if y + 2 <= 4:
        if item[x][y + 2] == "P" and item[x][y + 1] == "O":
            return 0
    #한 칸 오른쪽에 사람이 있는 경우
    if y + 1 <= 4 :
        if item[x][y + 1] == "P":
            return 0
    #오른 쪽 대각선에 사람이 있지만, 오른쪽과 밑에 파티션이 없을 경우
    if x + 1 <= 4 and y + 1 <= 4:
        if item[x+1][y+1] == "P":
            if item[x][y+1] == "O" or item[x+1][y] == "O":
                return 0
    #왼쪽 대각선에 사람이 있지만, 오른쪽과 밑에 파티션이 없을 경우
    if x + 1 <= 4 and y - 1 >= 0:
        if item[x+1][y-1] == "P":
            if item[x][y-1] == "O" or item[x+1][y] == "O":
                return 0

        
def solution(places):
    farAway = True
    answer = []
    for item in places:
        for x in range(5):
            for y in range(5):
                if item[x][y] == "P":
                    if check(x, y, item) == 0:
                        farAway = False
        if not farAway:
            answer.append(0)
            farAway = True
        else:
            answer.append(1)
        
                
    
    return answer