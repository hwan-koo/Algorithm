import math
def solution(brown, yellow):
    answer = []
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            width = yellow // i
            height = i
            if 2 * width + 2 * height + 4 == brown:
                answer.append(width + 2)
                answer.append(height + 2)
                break
    return answer