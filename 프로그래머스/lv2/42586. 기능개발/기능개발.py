import math
def solution(progresses, speeds):
    answer = []
    work = []
    for i in range(len(progresses)):
         work.append(math.ceil((100 - progresses[i]) / speeds[i]))
    print(work)
    count = 1
    temp = work[0]
    while work:
        now = work.pop(0)
        for i in work[:]:
            if now < i:
                answer.append(count)
                count = 1
                break
            else:
                count += 1
                work.pop(0)
        if not work:
            answer.append(count)
        
                
    
            
    return answer