def solution(arr, k):
    answer = []
    for i in arr:
        if len(answer) == k:
            break
        if i not in answer:
            answer.append(i)
    if len(answer) < k :
        for _ in range(k - len(answer)):
            answer.append(-1)
    
    return answer