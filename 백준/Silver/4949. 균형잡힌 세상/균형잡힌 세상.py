while True:
    question = list(input())
    stack = []
    if "".join(question) == ".":
        break
    for i in range(len(question)):
        if question[i] == "(":
            stack.append("(")
        if question[i] == "[":
            stack.append("[")
        if question[i] == ")":
            stack.append(")")
        if question[i] == "]":
            stack.append("]")
    answer = "".join(stack)
    time = 0
    while answer != "":
        answer = answer.replace("()", "")
        answer = answer.replace("[]", "")
        time += 1
        if time == 100:
            break
    if answer:
        print("no")
    else:
        print("yes")