def solution(s1, s2):
    
    answer = len(list(set(s1) & set(s2)))
    return answer