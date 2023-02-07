X = []
Y = []
for _ in range(3):
    a, b = map(int, input().split())
    X.append(a)
    Y.append(b)

for i in range(3):
    if X.count((X[i])) == 1:
        a = X[i]
    if Y.count((Y[i])) == 1:
        b = Y[i]
print(a,b)
    