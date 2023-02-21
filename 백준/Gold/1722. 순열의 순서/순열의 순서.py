N = int(input())
F = [0] * 21
S = [0] * 21
visited = [False] * 21
F[0] = 1
for i in range(1, N+1):
    F[i] = F[i-1] * i
input_list = list(map(int, input().split()))
if input_list[0] == 1:
    K = input_list[1]
    for i in range(1, N+1):
        count = 1
        for j in range(1, N+1):
            if visited[j]:
                continue
            if K <= count * F[N - i]:
                K -= (count - 1) * F[N - i]
                S[i] = j
                visited[j] = True
                break
            count += 1
    print(*S[1:N+1])
else:
    K = 1
    for i in range(1, N+1):
        count = 0
        for j in range(1, input_list[i]):
            if not visited[j]:
                count += 1
        K += count * F[N - i]
        visited[input_list[i]] = True
    print(K)
