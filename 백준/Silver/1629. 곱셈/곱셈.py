A, B, C = map(int, input().split())

def hb(A,B,C):
    if B == 1:
        return A % C
    else:
        next = hb(A, B // 2, C)
        if B % 2 == 0:
            return (next * next) % C
        else:
            return (next * next * A) % C
print(hb(A,B,C))