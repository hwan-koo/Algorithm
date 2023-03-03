def solution(name):
    answer = 0
    mi = len(name) - 1
    for i, alpha in enumerate(name):
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1 
        mi = min([mi, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
    answer += mi
    return answer