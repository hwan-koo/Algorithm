def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        temp = i
        for j in baby:
            if j in i:
                temp = temp.replace(j, "", 1)
        if temp == "":
            answer += 1
    
    return answer