import sys
answer = sys.maxsize
for _ in range(3):
    a = int(input())
    if a < answer:
        answer = a
cola = int(input())
cidar = int(input())
print(answer + min(cola,cidar) - 50)