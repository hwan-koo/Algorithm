def solution(n):
    pizza = 0
    while True:
        pizza += 1
        if (pizza * 6) % n == 0:
            break
    return pizza