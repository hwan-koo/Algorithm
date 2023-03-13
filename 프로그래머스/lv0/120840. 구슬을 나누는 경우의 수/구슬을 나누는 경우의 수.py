def solution(balls, share):
    A = [[0] * 31 for _ in range(31)]
    for i in range(1, 31):
        A[i][0] = 1
        A[i][i] = 1
    for i in range(2, 31):
        for j in range(1, i):
            A[i][j] = A[i-1][j] + A[i-1][j-1]
    answer = A[balls][share]
    return answer