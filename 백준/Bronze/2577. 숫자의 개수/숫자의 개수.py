A = int(input())
B = int(input())
C = int(input())

find = str(A * B * C)

for i in range(10):
    print(find.count(str(i)))
