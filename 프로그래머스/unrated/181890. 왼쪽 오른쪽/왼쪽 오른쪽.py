def solution(str_list):
    if str_list == ["l"]:
        return []
    elif str_list == ["u"]:
        return []
    ok = False
    for i in str_list:
        if i in ["l", "u"]:
            ok = True
    if not ok:
        return []
    for i in str_list:
        print(i)
        if i == "l":
            answer = str_list[:(str_list.index("l"))]
            break
        elif i == "r":
            answer = str_list[(str_list.index("r")+1):]
            break

    return answer