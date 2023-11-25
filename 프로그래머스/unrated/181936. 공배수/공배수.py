def solution(number, n, m):
    if (number % m == 0) and  (number % n == 0):
        return 1
    else:
        return 0