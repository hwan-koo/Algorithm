import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, category = map(str, input().split())
        if category not in dic:
            dic[category] = [name]
        else:
            dic[category].append(name)
    count = 1
    for i in dic:
        count *= (len(dic[i]) + 1)
    print(count - 1)