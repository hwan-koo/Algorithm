a, b = map(int, input().split())
casdc = list(map(int,input().split()))
answer = []
for i in casdc:
    answer.append(i - a * b)
print(*answer)