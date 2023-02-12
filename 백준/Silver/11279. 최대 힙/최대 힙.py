import sys
from queue import PriorityQueue
input = sys.stdin.readline
queue = PriorityQueue()
N = int(input())
for _ in range(N):
    a = int(input())
    if a > 0:
        queue.put(-a)
    else:
        if queue.empty():
            print(0)
        else:
            a = queue.get()
            print(-a)
