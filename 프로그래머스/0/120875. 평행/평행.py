def solution(dots):
    for i in range(3):
        for j in range(i+1, 4):
            dx1 = dots[j][0] - dots[i][0]
            dy1 = dots[j][1] - dots[i][1]
            temp = [0,1,2,3]
            temp.remove(i)
            temp.remove(j)
            c = temp[0]
            d = temp[1]
            dx2 = dots[d][0] - dots[c][0]
            dy2 = dots[d][1] - dots[c][1]
            if dx1/dy1 == dx2/dy2:
                return 1
    answer = 0
    return answer