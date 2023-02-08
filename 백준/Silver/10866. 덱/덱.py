import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()

for _ in range(N):
    order = input().split()
    if len(order) == 2:
        num = order[1]
        order = order[0]
    else:
        order = order[0]
    if order == "push_front":
        queue.appendleft(num)
    elif order == "push_back":
        queue.append(num)
    elif order == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)

