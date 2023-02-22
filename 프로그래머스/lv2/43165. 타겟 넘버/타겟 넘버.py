def solution(numbers, target):
    A = [0]
    answer = 0
    for i in numbers:
        temp = []
        for j in A:
            temp.append(j + i)
            temp.append(j - i)
        A = temp
    for i in A:
        if i == target:
            answer += 1
    return answer