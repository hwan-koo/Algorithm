import sys
input = sys.stdin.readline
S = str(input()).rstrip()
q = int(input())
A = [[0 for _ in range(len(S)+1)] for _ in range(26)]
for i in range(26):
    alphabet = chr(97 + i)
    for j in range(1, len(S)+1):
        if S[j-1] == alphabet:
            A[i][j] = A[i][j-1] + 1
        else:
            A[i][j] = A[i][j-1]

for _ in range(q):
    alpha, l, r = map(str, input().split())
    l = int(l)
    r = int(r)
    find = ord(alpha) - 97
    print(A[find][r+1] - A[find][l])

