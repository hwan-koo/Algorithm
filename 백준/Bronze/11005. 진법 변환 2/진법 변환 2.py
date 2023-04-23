n,b = map(int,input().split())
answer = ""
while n!=0:
    a = n % b
    if a >= 10:
        answer += chr(a+55)
    else:
        answer += str(a)
    n //= b
print(answer[::-1])