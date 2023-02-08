N, K = map(int, input().split())

A = list(range(1,N+1))
B = []
index = 0
while A:
    index += (K-1)
    if index > len(A)-1:
        index %= len(A)
    B.append(A.pop(index))


print("<",end="")
for i in range(len(B)):
    if i == len(B) - 1:
        print(B[i], end="")
    else:
        print(B[i], end=", ")
print(">")
