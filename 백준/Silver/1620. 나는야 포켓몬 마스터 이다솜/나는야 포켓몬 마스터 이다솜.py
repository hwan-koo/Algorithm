import sys

input = sys.stdin.readline
N, M = map(int, input().split())

poketmon = {}
for i in range(1, N + 1):
    poketmon_name = input().rstrip()
    poketmon[i] = poketmon_name
    poketmon[poketmon_name] = i

for _ in range(M):
    find = input().rstrip()
    if find.isdigit():
        print(poketmon[int(find)])
    else:
        print(poketmon[find])
