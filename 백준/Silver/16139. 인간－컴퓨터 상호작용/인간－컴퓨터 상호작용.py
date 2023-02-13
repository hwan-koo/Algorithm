import sys
input = sys.stdin.readline
S = str(input()).rstrip()
q = int(input())
A = [[0 for _ in range(len(S)+1)] for _ in range(26)]
for i in range(26):
    hb = 97 + i
    alphabet = chr(hb)
    temp = 0
    for j in range(1, len(S)+1):
        if S[j-1] == alphabet:
            temp += 1
            A[i][j] = temp
        else:
            A[i][j] = temp

for _ in range(q):
    alpha, l, r = map(str, input().split())
    l = int(l)
    r = int(r)
    find = ord(alpha) - 97
    haha = A[find][r+1]
    hoho = A[find][l]
    print(haha - hoho)

