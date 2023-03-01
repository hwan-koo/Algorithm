def solution(citations):
    answer = 0
    A = sorted(citations)
    h = 1
    go = []
    if max(citations) == 0:
        return 0
    while h <= max(citations):
        up = 0
        down = 0
        for i in A:
            if i >= h:
                up += 1
            else:
                down += 1
        if down <= h <= up:
            go.append(h)
        h += 1
    return max(go)