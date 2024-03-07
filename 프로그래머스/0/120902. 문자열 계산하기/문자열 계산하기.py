def solution(my_string):
    equation = my_string.split(" ")
    answer = 0
    minus = False
    for i in equation:
        if i == "+":
            continue
        elif i == "-":
            minus = True
        else:
            if minus:
                answer -= int(i)
                minus = False
            else:
                answer += int(i)
    return answer