N, k = map(int, input().split())
score_list = list(map(int, input().split()))

score_list.sort()
for _ in range(k-1):
    score_list.pop()
print(score_list.pop())