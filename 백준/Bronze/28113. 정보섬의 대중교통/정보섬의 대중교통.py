N, A, B = map(int, input().split())
if A < B:
    print("Bus")
elif A == B:
    if N <= A:
        print("Anything")
elif A > B :
    if N <= A:
        print("Subway")