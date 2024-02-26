def maxCommon(a,b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def minCommon(a,b):
    for i in range(max(a,b), (a*b) + 1):
        if i % a == 0 and i % b == 0:
            return i

def solution(numer1, denom1, numer2, denom2):
    lower = minCommon(denom1, denom2)
    a = lower // denom1
    b = lower // denom2
    upper = numer1 * a + numer2 * b
    answer = [upper // maxCommon(upper, lower), lower // maxCommon(upper,lower)]
    
    return answer