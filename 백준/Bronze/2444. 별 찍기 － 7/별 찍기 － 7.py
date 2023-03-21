N = int(input())
for i in range(1, 2 * N + 1):
    if i <= N:
        star = (N - i) * " " + (2 * i - 1) * "*"
    else:
        star = abs(N - i) * " " + (2 * N - 1 - 2 * (i - N)) * "*" 
    print(star)