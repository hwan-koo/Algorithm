N, K = map(int, input().split())
A = list(range(N+1))
count = 0
answer = [0]
for i in range(2, N+1):
    if A[i] == 0:
        continue
    for j in range(i, N+1, i):
        if A[j] == 0:
            continue
        A[j] = 0
        answer.append(j)
print(answer[K])