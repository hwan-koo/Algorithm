import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
A = list(input())
A.pop()
B = list(input())
B.pop()

D = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
answer = []

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:
            D[i][j] = D[i-1][j-1] + 1
        else:
            D[i][j] = max(D[i-1][j], D[i][j-1])

print(D[len(A)][len(B)])


def LCS(a, b):
    if a == 0 or b == 0:
        return
    if A[a - 1] == B[b -1]:
        answer.append(A[a - 1])
        LCS(a-1, b - 1)
    else:
        if D[a-1][b] > D[a][b-1]:
            LCS(a-1,b)
        else:
            LCS(a, b-1)
LCS(len(A), len(B))

for i in list(reversed(answer)):
    print(i, end="")