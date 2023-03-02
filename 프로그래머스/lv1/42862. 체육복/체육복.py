def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    uniform = [True] * (n+1)
    reserved = [True] * (n+1)
    uniform[0] = False
    for i in lost:
        uniform[i] = False
    for i in reserve:
        if i in lost:
            uniform[i] = True
        else:
            reserved[i] = False
    
    for i in lost:
        if (i - 1) in reserve:
            if not reserved[i-1]:
                uniform[i] = True
                reserved[i-1] = True
                continue
        if (i + 1) in reserve:
            if not reserved[i+1]:
                uniform[i] = True
                reserved[i+1] = True
    answer = 0
    for i in uniform:
        if i:
            answer += 1
    return answer