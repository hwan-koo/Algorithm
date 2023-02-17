n, k = map(int, input().split())
def answer(n, k):
    if n > k:
        return answer(k, k) + (n-k) * k
    i = 1
    result = n * k
    while i <= n:
        j = min(n, k // (k//i))
        result -= (k // i) * (j - i + 1) * (j + i) // 2
        i = j + 1
    return result
print(answer(n,k))