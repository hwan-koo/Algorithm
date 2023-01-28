N = int(input())
A = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
A.sort()
for i in range(M):
    target = M_list[i]
    start = 0
    end = len(A) - 1
    while start <= end:
        find = False
        mid_index = int((start + end) / 2)
        mid_value = A[mid_index]
        if mid_value > target:
            end = mid_index - 1
        elif mid_value < target:
            start = mid_index + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)


