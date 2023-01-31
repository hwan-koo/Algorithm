N = int(input())

p_list = []
for _ in range(N):
    x, y = map(int, input().split())
    p_list.append([x, y])

for i in p_list:
    rank = 1
    for j in p_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
