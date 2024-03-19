def solution(s):
    mini = len(s)
    
    
    for i in range(1, len(s) // 2 + 1):
        temp = ""
        coef = 1
        num = 0
        for j in range(0,len(s) + 1,i):
            if temp == s[j:j+i]:
                coef += 1
            else:
                num += len(s[j:j+i])
                if coef > 1:
                    num += len(str(coef))
                    coef = 1
                    temp = s[j:j+i]
                else:
                    temp = s[j:j+i]
                    
        mini = min(mini, num)
    return mini