import sys
input = sys.stdin.readline
K = int(input())
A = []
for _ in range(K):
    num = int(input())
    if num == 0:
        A.pop(-1)
    else:
        A.append(num)
print(sum(A))
