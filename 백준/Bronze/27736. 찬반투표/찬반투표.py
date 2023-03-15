N = int(input())
vote_list = list(map(int, input().split()))
yes = 0
no = 0
stop = 0

for i in vote_list:
    if i == 1:
        yes += 1
    if i == 0:
        stop += 1
    if i == -1:
        no += 1

while True:
    if N % 2 == 0:
        if stop >= N // 2:
            print("INVALID")
            break
    if N % 2 == 1:
        if stop >= N // 2 +1:
            print("INVALID")
            break
    if yes > no:
        print("APPROVED")
        break
    if no >= yes:
        print("REJECTED")
        break