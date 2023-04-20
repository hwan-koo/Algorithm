N = int(input())
tech = list(input())
stack = []
count = 0
for i in tech:
    if i == "R":
        if "L" in stack:
            stack.remove("L")
            count += 1
        else:
            break
    elif i == "K":
        if "S" in stack:
            stack.remove("S")
            count += 1
        else:
            break
    elif i == "L":
        stack.append("L")
    elif i == "S":
        stack.append("S")
    else:
        count += 1
print(count)