N = int(input())
M = int(input())
S = input()
PN = "IO" * N + "I"
count = 0
for i in range(M-len(PN)+1):
    if S[i:i+len(PN)] == PN:
        count += 1
print(count)