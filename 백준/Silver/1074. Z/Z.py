import sys
N, r, c = map(int, sys.stdin.readline().split())
answer = 0
while N != 0:
    N -= 1
    size = 2 ** N
    if r < size <= c:
        answer += size * size
        c -= size
    elif r >= size > c:
        answer += size * size * 2
        r -= size
    elif r >= size and c >= size:
        answer += size * size * 3
        r -= size
        c -= size
print(answer)