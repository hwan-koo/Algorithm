def solution(n):
    num = 2
    answer = []
    while n > 1:
        if n % num == 0:
            answer.append(num)
            n = n // num
        else:
            num += 1
    answer = sorted(list(set(answer)))
    return answer