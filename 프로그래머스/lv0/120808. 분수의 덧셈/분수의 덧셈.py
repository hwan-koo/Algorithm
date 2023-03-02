def solution(numer1, denom1, numer2, denom2):
    answer = []
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    bottom = int(denom1 * denom2 / gcd(denom1, denom2))
    top = (bottom // denom1) * numer1 + (bottom // denom2) * numer2
    if top == bottom:
        return [1,1]
    for i in range(2, max(top,bottom)):
        if top % i == 0 and bottom % i == 0:
            top = top // i
            bottom = bottom // i
    answer.append(top)
    answer.append(bottom)
    return answer