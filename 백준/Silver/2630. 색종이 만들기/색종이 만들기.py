import sys
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))
white = 0
blue = 0
def hb(x,y,N):
    global white,blue
    color = A[x][y]
    for i in range(x, x +N):
        for j in range(y, y+N):
            if color != A[i][j]:
                hb(x,y,N//2)
                hb(x,y + N//2, N//2)
                hb(x + N // 2, y + N // 2, N // 2)
                hb(x + N // 2, y , N // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

hb(0, 0, N)
print(white)
print(blue)