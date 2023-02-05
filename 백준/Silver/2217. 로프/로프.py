import sys
input = sys.stdin.readline
N = int(input())
w_list = []
for _ in range(N):
    w_list.append(int(input()))

answer = w_list[0]
w_list.sort(reverse=True)
for i in range(1, N):
        temp = w_list[i] * (i+1)
        if temp > answer :
            answer = temp
print(answer)
