number = 1
while True:
    
    numlist = list(map(int, input().split()))
    n = numlist.pop(0)
    if n == 0:
        break
    if n % 2 == 1:
        print(f"Case {number}:", end=" ")
        print(format(numlist[(n) // 2],".1f"))
        number += 1 
    else:
        print(f"Case {number}:", end=" ")
        print(float(format((numlist[n // 2] + numlist[(n-1) // 2]) / 2,".1f")))
        number += 1
    