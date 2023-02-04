N, M = map(int, input().split())
tree_height = list(map(int, input().split()))

s = 1
e = max(tree_height)
while s <= e:
    mid = (s + e) // 2
    sum = 0
    for i in tree_height:
        if i > mid:
            sum += i - mid
    if sum < M:
        e = mid - 1
    else:
        s = mid + 1
print(e)