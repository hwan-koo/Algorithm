def solution(today, terms, privacies):
    answer = []
    number = 0
    dic = {}
    now = list(today.split("."))
    for j in terms:
        a = list(j.split(" "))
        dic[a[0]] = a[1]
    for i in privacies:
        number += 1
        temp = list(i.split("."))
        year = temp[0]
        month = temp[1]
        day= temp[2][0:2]
        category = temp[2][-1]
        if int(month) + int(dic[category]) > 12:
            if (int(month) + int(dic[category])) % 12 == 0:
                new_month = 12
                new_year = int(year) + (int(month) + int(dic[category])) // 12 - 1
            else:
                new_year = int(year) + (int(month) + int(dic[category])) // 12
                new_month = (int(month) + int(dic[category])) % 12
        else:
            new_year = int(year)
            new_month = int(month) + int(dic[category])
        if day == "01":
            new_day = 28
            new_month -= 1
            if new_month == 12:
                new_year -= 1
        else:
            new_day = int(day) - 1
        if int(now[0]) > new_year:
            answer.append(number)
            continue
        if int(now[0]) == new_year and int(now[1]) > new_month:
            answer.append(number)
            continue
        if int(now[0]) == new_year and int(now[1]) == new_month and int(now[2]) > new_day:
            answer.append(number)
            continue
        
            
    return answer