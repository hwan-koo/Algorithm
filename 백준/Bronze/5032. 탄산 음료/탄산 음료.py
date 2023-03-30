e, f, c = map(int, input().split())
bottle = e + f
answer = 0
while bottle// c > 0:
    answer += bottle // c
    bottle = bottle // c + bottle % c
print(answer)