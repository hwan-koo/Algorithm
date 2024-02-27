def solution(array):
    numList = [0] * 1000
    for i in array:
        numList[i] += 1
    if numList.count(max(numList)) >=2:
        answer = -1
    else:
        answer = numList.index(max(numList))
    return answer