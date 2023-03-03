import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):
    operation = list(input().split())
    if len(operation) == 2:
        order = operation[0]
        num = operation[1]
    if len(operation) == 1:
        order = operation[0]
        num = 0
    num = int(num)
    if order == "add":
        S.add(num)
    if order == "remove":
        S.discard(num)
    if order == "check":
        if num in S:
            print(1)
        else:
            print(0)
    if order == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    if order == "all":
        S = set(list(range(1, 21)))
    if order == "empty":
        S.clear()
