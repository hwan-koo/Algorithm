import sys
from queue import PriorityQueue
input = sys.stdin.readline
N = int(input())
queue = PriorityQueue()
for _ in range(N):
    num = int(input())
    if num == 0:
        if queue.qsize() == 0:
            print(0)
        else:
            print(queue.get())
    else:
        queue.put(num)