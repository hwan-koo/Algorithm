N, M = map(int, input().split())
answer = [0] * N
for _ in range(M):
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        answer[i-1] = c
print(*answer)