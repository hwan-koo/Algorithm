N = int(input())
number_card = set(map(int, input().split()))
M = int(input())
find_list = list(map(int, input().split()))

for i in find_list:
    if i in number_card:
        print(1, end=" ")
    else:
        print(0, end=" ")


