N = int(input())
cute = 0
no = 0
for _ in range(N):
    a = int(input())
    if a == 0:
        no += 1
    else:
        cute += 1
if cute > no:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")