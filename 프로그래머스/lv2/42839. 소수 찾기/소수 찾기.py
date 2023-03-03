import math
def solution(numbers):
    answer = 0
    num_list = set()
    numbers = list(map(int, numbers))
    visited = [False] * len(numbers)
    A = []
    def word():
        if len(A) == k:
            num_list.add(int("".join(A)))
            return
        else:
            for i in range(len(numbers)):
                 if not visited[i]:
                    A.append(str(numbers[i]))
                    visited[i] = True
                    word()
                    visited[i] = False
                    A.pop()
                
    for i in numbers:
        num_list.add(i)
    for k in range(1, len(numbers)+1):
        word()
    num_list = list(num_list)
    
    def isprime(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return 0
        return 1
    anwer = 0
    for i in num_list:
        if i == 0 or i == 1:
            continue
        answer += isprime(i)
    return answer