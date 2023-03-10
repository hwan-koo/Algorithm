def solution(age):
    dic = {}
    dic[0] = "a"
    dic[1] = "b"
    dic[2] = "c"
    dic[3] = "d"
    dic[4] = "e"
    dic[5] = "f"
    dic[6] = "g"
    dic[7] = "h"
    dic[8] = "i"
    dic[9] = "j"
    answer = ''
    for i in str(age):
        answer += dic[int(i)]
    return answer