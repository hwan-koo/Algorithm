while True:
    a, b, c = input().split()
    b = int(b)
    c = int(c)
    if a == "#":
        break
    else:
        if b > 17 or c >= 80:
            print(a, "Senior")
        else:
            print(a, "Junior")
