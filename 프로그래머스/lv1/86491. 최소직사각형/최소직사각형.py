#항상 가로로 놓고 가로가 더 길게 해놓은 뒤 푸는 문제
def solution(sizes):
    w = []
    h = []
    for i in sizes:
        if i[0] > i[1]:
            w.append(i[0])
            h.append(i[1])
        else:
            w.append(i[1])
            h.append(i[0])
    answer = max(w) * max(h)
    return answer