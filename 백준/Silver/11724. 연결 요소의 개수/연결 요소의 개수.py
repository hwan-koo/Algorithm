import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())

visit_list = [False for _ in range(N+1)]
A = [[] for _ in range(N+1)]

# 연결된 노드에 True값 할당
def DFS(x):
    visit_list[x] = True
    for i in A[x]:
        if not visit_list[i]:
            DFS(i)

# 양방향 노드로 모두 저장
for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)
count = 0
for i in range(1, N+1):
    if not visit_list[i]:
        count += 1
        DFS(i)

print(count)