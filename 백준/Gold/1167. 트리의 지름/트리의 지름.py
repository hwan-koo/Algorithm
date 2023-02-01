from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]


#트리 데이터 저장
for _ in range(N):
    tree = list(map(int, input().split()))
    index = 0
    S = tree[index] # 정점 번호
    index += 1
    while True:
        E = tree[index]
        if E == -1:
            break
        V = tree[index + 1]
        A[S].append((E, V))
        index += 2


distance = [0] * (N +1)
visited = [False] * (N +1)


def BFS(v):
    myque = deque()
    myque.append(v)
    visited[v] = True
    while myque:
        now_node = myque.popleft()
        for i in A[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                myque.append(i[0])
                distance[i[0]] = distance[now_node] + i[1] # 거리정보 업데이트

BFS(1)

max_distance = 1

for i in range(2, N+1):
    if distance[max_distance] < distance[i]:
        max_distance = i

# 초기화 후 다시 탐색 진행
distance = distance = [0] * (N +1)
visited = [False] * (N +1)

BFS(max_distance)

distance.sort()
print(distance[N])

