import itertools
def solution(numbers):
    a = list(itertools.permutations(numbers, 2))
    answer = []
    for i in a:
        answer.append(i[0] + i[1])
    answer = sorted(list(set(answer)))
    
    return answer