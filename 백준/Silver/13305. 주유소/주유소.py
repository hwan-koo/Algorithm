N = int(input())
street_list = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
A = []
remove_list = []
for i in range(N-1):
    A.append((oil_price[i], street_list[i], i))

A.sort()

cost = 0
oil = 0
while A:
    a = A.pop(0)
    oil += a[1]
    for j in A:
        if j[2] > a[2]:
            oil += j[1]
            remove_list.append(j)
    for t in remove_list:
        A.remove(t)
    remove_list = []
    cost += a[0] * oil
    oil = 0
    A.sort()
print(cost)
