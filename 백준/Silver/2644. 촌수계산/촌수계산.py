n = int(input())
a, b = map(int,input().split())
m = int(input())
A = [[] for _ in range(n + 1)]
visited = [False] * (n+1)
answer = []


for _ in range(m):
    x, y = map(int, input().split())
    A[x].append(y)
    A[y].append(x)

def DFS(start, num):
    num += 1
    visited[start] = True
    if start == b:
        answer.append(num)
    for i in A[start]:
        if not visited[i]:
            DFS(i, num)
DFS(a,0)
if not answer:
    print(-1)
else:
    print(answer[0] - 1)