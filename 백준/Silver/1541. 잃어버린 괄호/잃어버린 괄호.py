equation = list(map(str, input().split("-")))


def minus_sum(x):
    return sum(list(map(int, x.split("+"))))


init = minus_sum(equation[0])
temp = 0
for i in range(1, len(equation)):
    temp += minus_sum(equation[i])
print(init - temp)
