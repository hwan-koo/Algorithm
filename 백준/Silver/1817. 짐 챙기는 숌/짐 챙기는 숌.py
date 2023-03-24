N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    book_list = list(map(int, input().split()))
    temp = 0
    answer = 1
    for i in book_list:
        temp += i
        if temp > M:
            temp = i
            answer += 1
    print(answer)