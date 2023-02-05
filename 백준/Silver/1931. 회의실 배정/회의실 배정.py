from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()
for _ in range(N):
    a, b = map(int, input().split())
    pq.put((b, a))

count = 0
end = -1
while pq.qsize() > 0:
    a = pq.get()
    if a[1] >= end:
        count += 1
        end = a[0]

print(count)



