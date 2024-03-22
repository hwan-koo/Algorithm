from collections import deque
def solution(begin, target, words):
    visited = [False] * len(words)
    answer = 0
    queue = deque()
    queue.append([begin,0])
    while queue:
        now = queue.popleft()
        print(now)
        if now[0] == target:
            answer = now[1]
            break
        for i, item in enumerate(words):
            temp = 0
            if not visited[i]:
                #단어가 한글자만 차이나는지 검사
                for j in range(len(now[0])):
                    if now[0][j] != item[j]:
                        temp += 1
                    if temp > 1:
                        break
            if temp == 1:
                print(item)
                queue.append([item,now[1] + 1])
                visited[i] = True
            
    
    return answer