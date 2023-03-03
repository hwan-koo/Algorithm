def solution(array):
    A = [0] * 1001
    for i in array:
        A[i] += 1
    ma = max(A)
    if A.count(ma) > 1:
        return -1
    else:
        return A.index(ma)