import itertools
def solution(k, dungeons):
    answer = 0
    #던전을 탐색하는 모든 경우의 수를 리스트로 담아내기
    allCases = itertools.permutations(dungeons, len(dungeons))
    
    #모든 경우의 수를 다 돌아보기
    for i in list(allCases):
        tempK = k
        tempA = 0
        for j in i:
            if tempK >= j[0]:
                tempK -= j[1]
                tempA += 1
            else:
                continue
        if tempA > answer:
            answer = tempA
    
    
    
    return answer