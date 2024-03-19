def solution(new_id):
    ab = ""
    # 1, 2단계 수행
    for i in new_id:
        if i.isupper() :
            ab += i.lower()
        else:
            if i not in ["-","_","."] and not i.islower() and not i.isdigit():
                continue
            else:
                ab += i
    c = ab[0]
    #3단계 수행
    for i in range(1, len(ab)):
        if ab[i-1] == "." and ab[i] == ab[i-1]:
            continue
        else:
            c+= ab[i]
    de = c
    #4단계,5단계 수행
    if de == "":
        de = "a"
    else:
        
        if de[0] == ".":
            if len(de) == 1:
                de = "a"
            else:
                de = de[1:]
        if de[-1] == ".":
            if len(de) == 1:
                de = "a"
            else:
                de = de[:-1]
    f = de
    #6단계 수행
    if len(f) >= 16:
        f = f[:15]
        if f[-1] == ".":
            f = f[:-1]
    
    #7단계 수행
    if len(f) <=2:
        temp = f[-1]
        while len(f) <3:
            f += temp
    answer = f
    return answer