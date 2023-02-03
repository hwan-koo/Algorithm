N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
find_list = list(map(int, input().split()))

A = [0] * 20000001

for i in card_list:
    A[i + 10000000] += 1

for j in find_list:
    print(A[j + 10000000],end=" ")
