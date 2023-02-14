N, M = map(int, input().split())
truth = list(map(int, input().split()))
T = truth[0]
truth.pop(0)
party = [[] for _ in range(M)]
parent = list(range(N+1))

for i in range(M):
    party[i] = list(map(int, input().split()))
    party[i].pop(0)


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
    


for i in range(M):
    p = party[i][0]
    for j in range(1, len(party[i])):
        union(p, party[i][j])

count = 0
for i in range(M):
    answer = True
    p = party[i][0]
    for j in range(len(truth)):
        if find(p) == find(truth[j]):
            answer = False
            break
    if answer:
        count += 1

print(count)