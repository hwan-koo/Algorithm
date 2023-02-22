a, b = map(int, input().split())

def yaksu(a, b):
    if b == 0:
        return a
    else:
        return yaksu(b, a % b)

gongbasu = a * b // yaksu(a,b)
print(yaksu(a,b))
print(gongbasu)