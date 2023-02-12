A = [0,1]
n = int(input())

for i in range(2, n+1):
    a = A[i-1] + A[i-2]
    A.append(a)
print(A[-1])

