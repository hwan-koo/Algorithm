while True:
    A = list(map(int,input().split()))
    if A == [0,0,0]:
        break
    bitbeon = max(A)
    A.remove(bitbeon)
    sum = 0
    for i in A:
        sum += i * i
    bitbeon = bitbeon * bitbeon
    if sum == bitbeon:
        print("right")
    else:
        print("wrong")
