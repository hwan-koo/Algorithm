import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def W(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return W(20,20,20)
    if D[a][b][c]:
        return D[a][b][c]
    if a < b < c:
        D[a][b][c] = W(a,b,c - 1) + W(a,b - 1,c - 1) - W(a,b - 1,c)
        return D[a][b][c]
    else:
        D[a][b][c] = W(a-1,b,c) + W(a-1,b-1,c) + W(a-1,b,c-1) - W(a-1,b-1,c-1)
        return D[a][b][c]
D = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {W(a,b,c)}")
