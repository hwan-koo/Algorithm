import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, find_index = map(int, input().split())
    importance_list = deque(map(int, input().split()))
    count = 0
    if len(importance_list) == 1:
        print(1)
    else:
        while importance_list:
            temp = list(importance_list)
            if len(temp) == 1:
                temp = temp[0]
            else:
                temp.pop(0)
                temp = max(temp)
            if importance_list[0] < temp:
                importance_list.append(importance_list.popleft())
                if find_index > 0:
                    find_index -= 1
                else:
                    find_index = len(importance_list) - 1
            else:
                importance_list.popleft()
                if find_index > 0:
                    find_index -= 1
                    count += 1
                else:
                    count += 1
                    print(count)
                    importance_list.clear()
