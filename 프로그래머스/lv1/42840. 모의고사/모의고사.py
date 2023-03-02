def solution(answers):
    answer = []
    A = []
    for i in range(1,len(answers)+1):
        go = i % 5
        if go == 0:
            go = 5
        A.append(go)
    count = 0
    for i in range(len(A)):
        if answers[i] == A[i]:
            count += 1
    answer.append(count)
    
    B = []
    dx = [1,3,4,5]
    k = 0
    for i in range(len(answers)):
        if i % 2 == 0:
            B.append(2)
        else:
            B.append(dx[k % 4])
            k += 1
            if k == 4:
                k = 0
    count = 0
    for i in range(len(answers)):
        if answers[i] == B[i]:
            count += 1
    answer.append(count)
    
    C = []
    dy = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        go = i % 10
        C.append(dy[go])
    count = 0
    for i in range(len(answers)):
        if answers[i] == C[i]:
            count += 1
    answer.append(count)
    ma = max(answer)
    hap = []
    for i in range(len(answer)):
        if answer[i] == ma:
            hap.append(i+1)
    return hap