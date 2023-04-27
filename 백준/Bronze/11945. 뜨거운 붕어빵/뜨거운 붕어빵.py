N, M = map(int, input().split())
for _ in range(N):
    num = list(input())
    print("".join(reversed(num)))