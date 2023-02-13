import sys,heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    mi = []
    ma = []
    k = int(input())
    visited = [False] * k
    for i in range(k):
        order, num = map(str,input().split())
        if order == "I":
            heapq.heappush(mi, (int(num), i))
            heapq.heappush(ma, (-int(num), i))
            visited[i] = True
        if order == "D":
            if int(num) == -1:
                while mi and not visited[mi[0][1]]:
                    heapq.heappop(mi)
                if mi:
                    visited[mi[0][1]] = False
                    heapq.heappop(mi)
            else:
                while ma and not visited[ma[0][1]]:
                    heapq.heappop(ma)
                if ma:
                    visited[ma[0][1]] = False
                    heapq.heappop(ma)
    while ma and not visited[ma[0][1]]:
        heapq.heappop(ma)
    while mi and not visited[mi[0][1]]:
        heapq.heappop(mi)
    if mi and ma:
        print(-ma[0][0], mi[0][0])
    else:
        print("EMPTY")
