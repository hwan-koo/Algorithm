def solution(n):
    def factorial(n):
        if n > 1:
            return n * factorial(n-1)
        else:
            return 1
    for i in range(1, 12):
        if factorial(i) > n:
            return (i-1)
    