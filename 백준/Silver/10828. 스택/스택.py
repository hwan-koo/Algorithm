import sys

input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order_list = list(input().split())
    if len(order_list) > 1:
        order = order_list[0]
        number = order_list[1]
    else:
        order = order_list[0]

    if order == "push":
        stack.append(number)
    if order == "top" :
        if stack:
            print(stack[-1])
        else:
            print(-1)
    if order == "size":
        print(len(stack))
    if order == "empty":
        if stack:
            print(0)
        else:
            print(1)
    if order == "pop":
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)