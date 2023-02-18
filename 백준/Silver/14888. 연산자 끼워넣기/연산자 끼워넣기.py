import sys
N = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
sys.setrecursionlimit(10 ** 6)
ma = -10 ** 9
mi = 10 ** 9
def DFS(nth, sum, plus, minus, multiply, divide):
    global ma, mi
    if nth == N:
        ma = max(sum, ma)
        mi = min(sum, mi)
        return
    if plus > 0:
        DFS(nth + 1, sum + numbers[nth], plus - 1, minus, multiply, divide)
    if minus > 0:
        DFS(nth + 1, sum - numbers[nth], plus, minus - 1, multiply, divide)
    if multiply > 0:
        DFS(nth + 1, sum * numbers[nth], plus, minus, multiply - 1, divide)
    if divide > 0:
        DFS(nth + 1, int(sum / numbers[nth]), plus, minus, multiply, divide - 1)
DFS(1, numbers[0], operations[0], operations[1], operations[2], operations[3])
print(ma)
print(mi)