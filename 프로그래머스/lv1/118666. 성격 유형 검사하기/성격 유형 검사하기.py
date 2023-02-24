def solution(survey, choices):
    answer = ''
    dict = {}
    dict["R"] = 0
    dict["T"] = 0
    dict["C"] = 0
    dict["F"] = 0
    dict["J"] = 0
    dict["M"] = 0
    dict["A"] = 0
    dict["N"] = 0
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] > 4:
            dict[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            dict[survey[i][0]] += 4 - choices[i]
    if dict["R"] >= dict["T"]:
        answer += "R"
    else:
        answer += "T"
    if dict["C"] >= dict["F"]:
        answer += "C"
    else:
        answer += "F"
    if dict["J"] >= dict["M"]:
        answer += "J"
    else:
        answer += "M"
    if dict["A"] >= dict["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer