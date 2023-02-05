from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    pq.put(int(input()))

data1 = 0
data2 = 0
temp = 0
while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp += data1 + data2
    pq.put(data1 + data2)

print(temp)
