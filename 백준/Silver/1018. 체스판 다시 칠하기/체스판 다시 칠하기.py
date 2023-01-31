N, M = map(int, input().split())

board = []

for _ in range(N):
    temp = input()
    A = []
    for i in temp:
        A.append(i)
    board.append(A)

chess = [["W","B"] * 4,["B","W"] * 4] * 4

i = 0
j = 0
count_list = []
for i in range(N-7):
    for j in range(M-7):
        count_white = 0
        count_black = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "W":
                        count_white += 1
                    if board[a][b] != "B":
                        count_black += 1
                else:
                    if board[a][b] != "B":
                        count_white += 1
                    if board[a][b] != "W":
                        count_black += 1
        count_list.append(min(count_white, count_black))

print(min(count_list))
