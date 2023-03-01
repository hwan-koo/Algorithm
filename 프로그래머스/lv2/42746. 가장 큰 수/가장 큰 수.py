def solution(numbers):
    answer = ''
    A = list(map(str, numbers))
    A.sort(key=lambda  x: x * 3, reverse=True)
    answer = str(int("".join(A)))
    return answer