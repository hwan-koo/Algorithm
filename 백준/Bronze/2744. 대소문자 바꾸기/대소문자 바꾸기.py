a = input()
answer =""
for i in a:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()
print(answer)