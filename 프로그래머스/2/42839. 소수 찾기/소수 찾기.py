import itertools
def decimalCheck(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    candidateList = []
    temp = ""
    for i in range(1, len(numbers) + 1):
        permu = itertools.permutations(list(numbers),i)
        for j in permu:
            temp = int("".join(j))
            if temp not in candidateList:
                candidateList.append(temp)
    for i in candidateList:
        if decimalCheck(i):
            answer += 1
    
    
    return answer