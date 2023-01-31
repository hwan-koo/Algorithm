import sys
N, M = map(int, input().split())
sys.setrecursionlimit(10 ** 6)

num_list = list(map(int, input().split()))
sum_list = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_num = num_list[i] + num_list[j] + num_list[k]
            sum_list.append(sum_num)

filter_sum_list = [n for n in sum_list if n <= M]
print(max(filter_sum_list))
