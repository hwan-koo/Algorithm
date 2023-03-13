def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer += "0"
        if i == "0":
            answer += "5"
        if i == "5":
            answer += "2"
    return answer