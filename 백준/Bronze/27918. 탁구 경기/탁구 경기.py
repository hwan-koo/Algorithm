import sys
input = sys.stdin.readline
N = int(input())
dalgu = 0
ponix = 0

for _ in range(N):
    winner = str(input()).rstrip()
    if winner == "D":
        dalgu += 1
    else:
        ponix += 1
    if dalgu + 2 == ponix:
        break
    if ponix + 2 == dalgu:
        break
print(f"{dalgu}:{ponix}")