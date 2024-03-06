def solution(score):
    temp = []
    for i, item in enumerate(score):
        temp.append([(item[0] + item[1])/2,i])
    temp.sort(reverse=True)
    answer = [0] * len(score)
    for i in range(len(score)):
        if i >= 1:
            if temp[i][0] == temp[i-1][0]:
                answer[temp[i][1]] = answer[temp[i-1][1]]
            else:
                answer[temp[i][1]] = i + 1
        else:
            answer[temp[i][1]] = i + 1
    return answer