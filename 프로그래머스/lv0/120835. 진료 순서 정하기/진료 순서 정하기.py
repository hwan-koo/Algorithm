def solution(emergency):
    answer = [0] * len(emergency)
    A = emergency[:]
    emergency.sort(reverse=True)
    rank = 1
    for i in emergency:
        answer[A.index(i)] = rank
        rank += 1
    return answer