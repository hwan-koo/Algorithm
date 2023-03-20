answer = []
for _ in range(5):
    answer.append(sum(list(map(int, input().split(" ")))))
num = answer.index(max(answer))
score = answer[num]
print(num + 1, score)