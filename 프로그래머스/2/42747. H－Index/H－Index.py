def solution(citations):
    a = sorted(citations)
    min = 0
    for h in range(0, max(a) + 1):
        if h not in a:
            a.append(h)
            a.sort()
            if len(a) - a.index(h) - 1 >= h:
                min = h
            a.remove(h)
        else:
            if len(a) - a.index(h) >= h:
                min = h
    print(min)
    return min