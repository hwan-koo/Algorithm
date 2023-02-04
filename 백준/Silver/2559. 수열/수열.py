from collections import deque

N, K = map(int, input().split())
temper_list =list(map(int, input().split()))
myque = deque(temper_list[:K])
max = sum(myque)
hap = sum(myque)
index = 0
while index + K != N:
    hap -= myque.popleft()
    hap += temper_list[index + K]
    if max < hap:
        max = hap
    myque.append(temper_list[index + K])
    index += 1
print(max)