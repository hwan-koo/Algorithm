N = int(input())
sum = 1
for i in range(1,N+1):
    sum *= i
sum = str(sum)
if sum[-1] != "0":
    print(0)
else:
    count = 0
    for j in range(len(sum) - 1, -1, -1):
        if sum[j] == "0":
            count += 1
        else:
            break
    print(count)