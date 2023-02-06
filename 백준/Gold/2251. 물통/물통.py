from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

volume =list(map(int, input().split()))
send = [0,0,1,1,2,2]
receive = [1,2,0,2,0,1]
visited = [[False for _ in range(201)] for _ in range(201)]
answer = [False] * 201

def BFS():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    answer[volume[2]] = True
    while queue:
        now_node = queue.popleft()
        a = now_node[0]
        b = now_node[1]
        c = volume[2] - a - b
        for k in range(6):
            next = [a,b,c]
            next[receive[k]] += next[send[k]]
            next[send[k]] = 0
            if next[receive[k]] > volume[receive[k]]:
                next[send[k]] = next[receive[k]] - volume[receive[k]]
                next[receive[k]] = volume[receive[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0:
                    answer[next[2]] = True


BFS()

for i in range(len(answer)):
    if answer[i]:
        print(i, end=" ")