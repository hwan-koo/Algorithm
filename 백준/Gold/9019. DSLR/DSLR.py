import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    queue = deque()
    queue.append((A, ""))
    visited[A] = True
    while queue:
        now, answer = queue.popleft()
        for k in range(4):
            if k == 0:
                if now * 2 > 9999:
                    if not visited[(now * 2) % 10000]:
                        visited[(now * 2) % 10000] = True
                        if (now * 2) % 10000 == B:
                            print(answer + "D")
                            queue.clear()
                            break
                        queue.append(((now * 2) % 10000, answer + "D"))
                else:
                    if not visited[now * 2]:
                        visited[now * 2] = True
                        if now * 2 == B:
                            print(answer + "D")
                            queue.clear()
                            break
                        queue.append((now * 2, answer + "D"))

            if k == 1:
                if now == 0:
                    if not visited[9999]:
                        visited[9999] = True
                        if 9999 == B:
                            print(answer + "S")
                            queue.clear()
                            break
                        queue.append((9999, answer + "S"))
                else:
                    if not visited[now - 1]:
                        visited[now - 1] = True
                        if now - 1 == B:
                            print(answer + "S")
                            queue.clear()
                            break
                        queue.append((now - 1, answer + "S"))
            if k == 2:
                L = (10 * now + (now // 1000)) % 10000
                if not visited[L]:
                    visited[L] = True
                    if L == B:
                        print(answer + "L")
                        queue.clear()
                        break
                    queue.append((L, answer + "L"))

            if k == 3:
                R = (now // 10 + (now % 10) * 1000) % 10000
                if not visited[R]:
                    visited[R] = True
                    if R == B:
                        print(answer + "R")
                        queue.clear()
                        break
                    queue.append((R,answer + "R"))
