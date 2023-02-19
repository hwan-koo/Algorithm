import sys
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
answer = []
def hb(x, y, N):
    global answer
    color = A[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != A[i][j]:
                hb(x, y, N //3)
                hb(x, y + N//3, N//3)
                hb(x, y + 2 * N // 3, N // 3)
                hb(x + N // 3, y, N // 3)
                hb(x + 2 * N // 3, y, N // 3)
                hb(x + N // 3, y + N // 3, N // 3)
                hb(x + 2 * N // 3, y + N // 3, N // 3)
                hb(x + N // 3, y + 2 * N // 3, N // 3)
                hb(x + 2 * N // 3, y + 2 * N // 3, N // 3)
                return
    answer.append(color)
hb(0, 0, N)
print(answer.count(-1))
print(answer.count(0))
print(answer.count(1))