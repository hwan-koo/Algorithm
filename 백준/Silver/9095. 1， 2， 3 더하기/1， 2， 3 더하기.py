T = int(input())


def ans(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return ans(n-1) + ans(n-2) + ans(n-3)


for _ in range(T):
    n = int(input())
    print(ans(n))