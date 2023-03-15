import math
def isprime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count >= 3:
        return 1
    else:
        return 0
def solution(n):
    answer = 0
    for i in range(1, n+1):
        answer += isprime(i)
    return answer