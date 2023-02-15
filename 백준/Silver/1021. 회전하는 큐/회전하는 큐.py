from collections import deque
N, M = map(int, input().split())
find = list(map(int, input().split()))
queue = deque()
for i in range(1, N+1):
    queue.append(i)
count = 0
while find:
    target = find[0]
    a = queue.popleft()
    if target == a:
        find.pop(0)
        continue
    else:
        if queue.index(target) >= len(queue) // 2:
            queue.appendleft(a)
            temp = queue.pop()
            queue.appendleft(temp)
            count += 1
        else:
            queue.append(a)
            count += 1
print(count)