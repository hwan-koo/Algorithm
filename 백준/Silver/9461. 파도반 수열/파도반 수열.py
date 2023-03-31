T = int(input())
A = [1,1,1,2,2,3,4,5,7,9] + [0] * 91

for i in range(10, 101):
    A[i] = A[i-1] + A[i-5]
for _ in range(T):
    N = int(input())
    print(A[N-1])