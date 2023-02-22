import sys
sys.setrecursionlimit(10 ** 6)
def solution(n, computers):
    answer = 0
    visited = [False] * n
    def DFS(x):
        visited[x] = True
        for i in range(len(computers[x])):
            if i == x:
                continue
            if not visited[i]:
                if computers[x][i] == 1:
                    DFS(i)
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
        
                
    return answer