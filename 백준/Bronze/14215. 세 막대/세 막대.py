a, b, c = map(int, input().split())
ma = max(a,b,c)
find = [a,b,c]
find.remove(ma)
if sum(find) <= ma:
    answer = sum(find) * 2 - 1
else:
    answer = sum(find) + ma
print(answer)