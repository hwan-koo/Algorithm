import sys
input = sys.stdin.readline
A = []
for i in range(1,9):
    A.append((int(input()),i))

A.sort(reverse=True)
B = A[0:5]
B.sort(key=lambda x:x[1])
sum = 0
for i in B:
    sum += i[0]
print(sum)
for i in B:
    print(i[1],end=" ")