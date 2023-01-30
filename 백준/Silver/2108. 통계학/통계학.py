import math
import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))
average = round((sum(num_list) / N))
num_list.sort()
median = num_list[int(math.floor(((N - 1) / 2)))]
num_range = max(num_list) - min(num_list)
print(average)
print(median)
#최빈값 구하기
if N == 1:
    print(average)
else:
    count_list = Counter(num_list).most_common()
    count_list.sort()
    count_list.sort(key=lambda x:x[1], reverse=True)
    if count_list[0][1] == count_list[1][1]:
        print(count_list[1][0])
    else:
        print(count_list[0][0])
print(num_range)