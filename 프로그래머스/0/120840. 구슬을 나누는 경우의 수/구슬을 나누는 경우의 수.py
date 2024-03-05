def solution(balls, share):
    temp1 = 1
    for i in range(1, balls+1):
        temp1 *= i
    temp2 = 1
    for i in range(1, balls + 1 - share):
        temp2 *= i
    temp3 = 1
    for i in range(1, share + 1):
        temp3 *= i
    
    answer = temp1 // (temp2 * temp3)
    return answer