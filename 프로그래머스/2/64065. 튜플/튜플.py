def solution(s):
    s = s[1:-1].split("{")
    s.sort(key=len)
    temp = ""
    answer = []
    for i in s:
        for j in i:
            if j == "":
                continue
            elif j == "}":
                if temp != "" and int(temp) not in answer:
                    answer.append(int(temp))
                    temp = ""
                else:
                    temp = ""
            elif j == ",":
                if temp != "" and int(temp) not in answer:
                    answer.append(int(temp))
                    temp = ""
                else:
                    temp = ""
            else:
                temp += j
    
    return answer