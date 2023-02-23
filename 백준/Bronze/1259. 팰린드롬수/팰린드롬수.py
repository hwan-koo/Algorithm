while True:
    test = input()
    if test == "0":
        break
    if "".join(reversed(list(test))) == test:
        print("yes")
    else:
        print("no")