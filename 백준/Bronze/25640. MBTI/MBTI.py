MBTI = input()
N = int(input())
answer = 0
for _ in range(N):
    find = input()
    if MBTI == find:
        answer += 1
print(answer)