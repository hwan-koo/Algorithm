N = int(input())
tops = list(map(int, input().split()))
tops.reverse()
stack = []
signal = [0] * N
for i in range(N):
    while stack and tops[stack[-1]] < tops[i]:
        signal[stack.pop()] = N - i
    stack.append(i)
signal.reverse()
print(*signal)