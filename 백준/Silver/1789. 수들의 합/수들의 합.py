S = int(input())


x = 1
index = 1

def sam(x):
    return (x * (x+1)) // 2

index = 1
while sam(index) <= S:
    index += 1
if S == 1:
    print(1)
else:
    print(index - 1)
