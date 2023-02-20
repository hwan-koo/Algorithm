import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
visited = [False] * N
A = []
B = set()
def DFS(k):
    if len(A) == M:
        B.add(tuple(A))
        return
    for i in range(k,len(input_list)):
        if not visited[i]:
            A.append(input_list[i])
            DFS(i)
            A.pop()
DFS(0)
answer = list(B)
answer.sort()
for i in answer:
    print(*i)
