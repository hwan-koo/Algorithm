a, b, c = map(int, input().split())
dic = {a: "Soongsil", b: "Korea", c: "Hanyang"}

if a + b + c >= 100:
    print("OK")
else:
    print(dic[min(a,b,c)])