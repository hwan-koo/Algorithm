def hanoi(n, start, end, mid, answer):
    if n == 1:
        return answer.append([start, end])
    # n-1개의 원판을 3번을 경유하여 2번에 옮기기
    hanoi(n - 1, start, mid, end, answer)
    #제일 큰 원판을 3번에 옮기기
    answer.append([start, end])
    # n-1개의 원판을 2번에서 1번을 경유하여 3번으로 옮기기
    hanoi(n - 1, mid, end, start, answer)
    
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer