def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
def solution(N):
    for i in range(10, 0, -1):
        if factorial(i) <= N:
            answer = i
            break
    return answer