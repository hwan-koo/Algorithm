M, N = map(int,input().split())


def isPrime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
        else:
            continue
    return True


for i in range(M, N+1):
    if i == 1:
        continue
    if isPrime(i):
        print(i)
