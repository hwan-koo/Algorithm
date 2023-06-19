import math
L = int(input())
a = int(input())
b = int(input())
c = int(input())
e = int(input())

f = math.ceil(a/c)
g = math.ceil(b/e)

if f > g:
    print(L - f)
else:
    print(L - g)
