while True:
    answer = 0
    a = list(input())
    if a[0] == "#":
        break
    else:
        for i in a:
            if i.lower() in ["a", "e", "i", "o", "u"]:
                answer += 1
    print(answer)
