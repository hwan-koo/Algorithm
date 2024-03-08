def solution(my_string):
    answer = 0
    temp = ""
    for i in my_string:
        
        if i.isdigit():
            temp += i
            print(temp)
        else:
            if temp != "":
                answer += int(temp)
                temp = ""
    if temp != "":
        answer += int(temp)
    return answer