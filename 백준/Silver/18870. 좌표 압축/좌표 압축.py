import sys
input = sys.stdin.readline

N = int(input())
x_list = list(map(int, input().split()))
temp = []
for i in range(N):
    temp.append((x_list[i], i))
temp.sort()
# 값, 원래의 Index, 등수
stack = [[0, 0, 0] for _ in range(N)]
stack[0][0] = temp[0][0]
stack[0][1] = temp[0][1]
# 등수 로직
for i in range(1, N):
    stack[i][0] = temp[i][0]
    stack[i][1] = temp[i][1]
    if stack[i][0] == stack[i-1][0]:
        stack[i][2] = stack[i-1][2]
    else:
        stack[i][2] = stack[i - 1][2] + 1
stack.sort(key=lambda x:x[1])
for i in range(N):
    print(stack[i][2], end= " ")