from itertools import combinations
tall = []
for _ in range(9):
    tall.append(int(input()))

for i in combinations(tall, 7):
    if sum(i) == 100:
        answer = sorted(list(i))
        break
for i in answer:
    print(i)
