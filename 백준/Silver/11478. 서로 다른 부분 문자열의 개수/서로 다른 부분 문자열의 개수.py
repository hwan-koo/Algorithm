S = input()
A = []
for i in range(len(S)):
    for j in range(len(S)):
        A.append(S[i:j+1])
A = set(A)
A.remove("")
print(len(set(A)))