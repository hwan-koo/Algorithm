answer = [0] * 26
for i in input():
    answer[ord(i)-97] += 1
print(*answer)