def solution(numbers):
    dic  = {
        "zero" : 0, "one": 1, "two" : 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    temp = []
    answer = ""
    for i in numbers:
        temp.append(i)
        if "".join(temp) in dic:
            answer  += str(dic["".join(temp)])
            temp = []
    if answer[0] == 0:
        answer.pop(0)
    return int(answer)