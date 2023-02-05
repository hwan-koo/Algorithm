from queue import PriorityQueue
N = int(input())
plus_pq = PriorityQueue()
minus_pq = PriorityQueue()
one = 0
zero = 0
for _ in range(N):
    k = int(input())
    if k > 1:
        plus_pq.put(k * -1)
    elif k <= -1 :
        minus_pq.put(k)
    elif k == 1:
        one += 1
    elif k == 0:
        zero += 1

sum = 0

while plus_pq.qsize() > 1:
    a = plus_pq.get()
    b = plus_pq.get()
    sum += a * b
if plus_pq.qsize() == 1:
    sum += plus_pq.get() * -1

while minus_pq.qsize() > 1:
    a = minus_pq.get()
    b = minus_pq.get()
    sum += a * b
if minus_pq.qsize() == 1:
    if zero == 0:
        sum += minus_pq.get()

sum += one
print(sum)


