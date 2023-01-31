import sys
N, M = map(int, input().split())

num_list = list(map(int, input().split()))
sum_list = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_num = num_list[i] + num_list[j] + num_list[k]
            if sum_num <= M:
                sum_list.append(sum_num)

print(max(sum_list))
