answer = 0
cre = []
for _ in range(7):
    a = int(input())
    if a % 2 == 1:
        answer += a
        cre.append(a)



if answer == 0:
    print(-1)
else:
    print(answer)
    print(min(cre))