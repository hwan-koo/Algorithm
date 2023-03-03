def solution(number, k):
    A = []
    for i in number:
        while A and A[-1] < i and k >0:
            A.pop()
            k -=1
        A.append(i)
    if k > 0:
        A = A[:-k]
    answer = str("".join(A))
    return answer
