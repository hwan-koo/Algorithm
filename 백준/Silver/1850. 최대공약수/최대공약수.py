def yaksu(a, b):
    if b == 0:
        return a
    else:
        return yaksu(b, a % b)
a, b = map(int, input().split())
answer = yaksu(a, b)
while answer > 0:
    print(1, end="")
    answer -= 1