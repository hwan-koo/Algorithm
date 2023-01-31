import sys
N = int(input())
sys.setrecursionlimit(10 ** 6)


def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def surprise_prime(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if is_prime(number * 10 + i):
                surprise_prime(number * 10 + i)


surprise_prime(2)
surprise_prime(3)
surprise_prime(5)
surprise_prime(7)



