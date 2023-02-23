from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque()
    visited = [False] * len(words)
    def BFS(x):
        global answer
        queue.append((x,0))
        while queue:
            now = queue.popleft()
            find = now[0]
            count = now[1]
            for i in range(len(words)):
                if not visited[i]:
                    temp = 0
                    for k in range(len(find)):
                        if find[k] == words[i][k]:
                            temp += 1
                    if temp == len(find) - 1:
                        visited[i] = True
                        count += 1
                        if words[i] == target:
                            answer = count
                            return answer
                        queue.append((words[i],count))
    answer = BFS(begin)
    if answer:
        return answer
    else:
        return 0