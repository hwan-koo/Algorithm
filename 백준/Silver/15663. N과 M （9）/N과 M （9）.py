import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
visited = [False] * N
A = []
B = set()
def DFS():
    if len(A) == M:
        B.add(tuple(A))
        return
    for i in range(len(input_list)):
        if not visited[i]:
            A.append(input_list[i])
            visited[i] = True
            DFS()
            visited[i] = False
            A.pop()
DFS()
answer = list(B)
answer.sort()
for i in answer:
    print(*i)