while True:
    a = input()
    if int(a) == 0:
        break
    answer = 0
    for i in list(a):
        if i == "1":
            answer += 3
        elif i == "0":
            answer += 5
        else:
            answer += 4
    answer += 1
    print(answer)
