T = int(input())
def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(num(M,N,x,y))

