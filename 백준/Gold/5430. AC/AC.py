T = int(input())

for _ in range(T):
    function = input()
    n = int(input())
    A = input().replace("[","").replace("]","").split(",")
    p = True
    reverse = 0
    if A == [""]:
        A = []
    for i in function:
        if i == "R":
            reverse += 1
        elif i == "D":
            if reverse % 2 == 1:
                if not A:
                    print("error")
                    p = False
                    break
                A.pop()
            else:
                if not A:
                    print("error")
                    p = False
                    break
                A.pop(0)
    if reverse % 2 == 1:
        A.reverse()
    if p:
        print("[",end="")
        for i in range(len(A)):
            if i == len(A) - 1:
                print(A[i],end="")
            else:
                print(A[i], end=",")
        print("]")
    else:
        continue

