N = int(input())
milk_list = list(map(int, input().split()))

answer = 0

for i in milk_list:
    if answer % 3 == 0:
        if i == 0:
            answer += 1
        else:
            continue
    elif answer % 3 == 1:
        if i == 1:
            answer += 1
        else:
            continue
    else:
        if i == 2:
            answer += 1
        else:
            continue
print(answer)