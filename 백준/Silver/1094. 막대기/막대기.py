X = int(input())

stick = 64
sticks = [64]

while sum(sticks) != X:
    if sum(sticks) > X:
        sticks.remove(stick)
        stick = stick // 2
        sticks.append(stick)
        if sum(sticks) < X:
            sticks.append(stick)
print(len(sticks))
