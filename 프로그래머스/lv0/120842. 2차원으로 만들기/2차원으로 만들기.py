def solution(num_list, n):
    answer = []
    index = 1
    temp = []
    for i in num_list:
        temp.append(i)
        if index == n:
            answer.append(temp)
            temp = []
            index = 1
            continue
        index += 1
    return answer