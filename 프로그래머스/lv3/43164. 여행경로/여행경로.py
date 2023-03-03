def solution(tickets):
    answer = []
    routes = {}
    for i, j in tickets:
        routes[i] = routes.get(i, []) + [j]
    for i in routes.keys():
        routes[i].sort(reverse=True)
    stack = ["ICN"]
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    answer.reverse()
    return answer