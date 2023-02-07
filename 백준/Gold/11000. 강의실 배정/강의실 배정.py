import sys
from queue import PriorityQueue
input = sys.stdin.readline
N = int(input())
A = [[0] * 2 for _ in range(N)]
for i in range(N):
    s, e = map(int, input().split())
    A[i][0] = s
    A[i][1] = e
A.sort()
queue = PriorityQueue()
queue.put(A[0][1])
for i in range(1, N):
    a = queue.get()
    if a <= A[i][0]:
        queue.put(A[i][1])
    else:
        queue.put(a)
        queue.put(A[i][1])
print(queue.qsize())
