def solution(sides):
    answer = []
#     주어진 길이중 하나가 가장 긴 변인 경우
    for i in range(1, max(sides)+1):
        if i + min(sides) > max(sides):
            answer.append(i)
    num = max(sides) 
    while sum(sides) > num:
        answer.append(num)
        num += 1
    
    return len(list(set(answer)))