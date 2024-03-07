def solution(cipher, code):
    num = 1
    answer = ''
    for i in cipher:
        if num == code:
            answer += i
            num = 1
        else:
            num += 1
    
    return answer