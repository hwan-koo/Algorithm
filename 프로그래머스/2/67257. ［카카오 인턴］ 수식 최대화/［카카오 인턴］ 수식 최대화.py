def solution(expression):
    answer_list = []
    #숫자와 연산자 분리
    str_temp = ""
    expression_list = []
    for i in expression:
        if i not in ["-", "*", "+"]:
            str_temp += i
        else:
            expression_list.append(int(str_temp))
            expression_list.append(i)
            str_temp = ""
    expression_list.append(int(str_temp))
    
    #연산 함수
    def compute(expression, operator):
        count = False
        count_wait = []
        for i in range(len(expression)):
            if count == True:
                count = False
                continue
            if expression[i] == operator:
                if operator == "*":
                    count_wait.append(count_wait.pop() * expression[i + 1])
                elif operator == "+":
                    count_wait.append(count_wait.pop() + expression[i + 1])
                else:
                    count_wait.append(count_wait.pop() - expression[i + 1])
                count = True
            else:
                count_wait.append(expression[i])
        return count_wait
    
    x = compute(expression_list, "*")
    xp = compute(x, "+")
    xpm = compute(xp, "-")
    xm = compute(x, "-")
    xmp = compute(xm, "+")
    
    p = compute(expression_list, "+")
    px = compute(p, "*")
    pxm = compute(px, "-")
    pm = compute(p, "-")
    pmx = compute(pm, "*")
    
    m = compute(expression_list, "-")
    mx = compute(m, "*")
    mxp = compute(mx, "+")
    mp = compute(m, "+")
    mpx = compute(mp, "*")
    
    
    
    
    answer_list = max([abs(xpm[0]),abs(xmp[0]),abs(pmx[0]),abs(pxm[0]),abs(mxp[0]), abs(mpx[0])])
    

    return answer_list