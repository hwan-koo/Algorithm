a = input()
explosion = input()
stack = []
for i in a:
    stack.append(i)
    if "".join(stack[-len(explosion):]) == explosion:
        stack[-len(explosion):] = []
if stack:
    print("".join(stack))
else:
    print("FRULA")