N = int(input())
M = int(input())
S = input()
PN = ["I", "O"] * N
PN.append("I")
count = 0
temp = list(S[:2 * N + 1])
if temp == PN:
    count += 1
for i in range(2 * N + 1, M):
    temp.pop(0)
    temp.append(S[i])
    if temp == PN:
        count += 1
print(count)