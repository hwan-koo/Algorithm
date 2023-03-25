for _ in range(3):
    play = list(map(int, input().split()))
    front = play.count(0)
    if front == 1:
        print("A")
    if front == 0:
        print("E")
    if front == 2:
        print("B")
    if front == 3:
        print("C")
    if front == 4:
        print("D")