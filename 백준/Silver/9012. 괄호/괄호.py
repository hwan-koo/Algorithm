T = int(input())

for _ in range(T):
    string = str(input()).rstrip()
    time = 0
    while string != "":
        string = string.replace("()", "")
        time += 1
        if time == 100:
            break
    if string != "":
        print("NO")
    else:
        print("YES")