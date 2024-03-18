def solution(s):
    answer = ''
    array = s.split(" ")
    for i in array:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()        
            else:
                answer += i[j].lower()
        answer += " "
        
    
    return answer[:-1]