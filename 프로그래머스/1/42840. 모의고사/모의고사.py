def solution(answers):
    first = 0
    firstList = [1, 2, 3, 4, 5]
    second = 0
    secondList = [2, 1, 2, 3, 2, 4, 2, 5]
    third = 0
    thirdList = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, item in enumerate(answers):
        if item == firstList[i % 5]:
            first += 1
    for i, item in enumerate(answers):
        if item == secondList[i % 8]:
            second += 1
    for i, item in enumerate(answers):
        if item == thirdList[i % 10]:
            third += 1
    candidate = [first, second, third]
    answer = []
    if candidate.count(max(candidate)) > 1:
        for i,item in enumerate(candidate):
            if item == max(candidate):
                answer.append(i + 1)
    else:
        answer.append(candidate.index(max(candidate)) + 1)
                
    return answer