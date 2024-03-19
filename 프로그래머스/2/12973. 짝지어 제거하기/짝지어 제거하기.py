def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) >= 2:
            while True:
                if len(stack) < 2:
                    break
                if stack[-1] == stack[-2]:
                    stack.pop(-1)
                    stack.pop(-1)
                else:
                    break
                
                
    if stack == []:
        return 1
    else:

        return 0