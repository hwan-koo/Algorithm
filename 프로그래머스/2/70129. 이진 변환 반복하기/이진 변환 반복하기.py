def solution(s):
    count = 0
    zero = 0
    while s != "1":
        temp = 0
        for i in s:
            if i == "0":
                temp += 1
        zero += temp
        s = bin(len(s) - temp)[2:]
        
        count += 1
        
                
    
    answer = [count,zero]
    return answer