from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    
    for a, b in tickets:
        graph[a].append(b)
    for key in graph.keys():
        graph[key].sort()
    
    def DFS(graph, path, visit):
        if path:
            #출발지 지정
            to = path[-1]
            print(to)
            # 방문 처리
            if graph[to]:
                path.append(graph[to].pop(0))
            else:
                visit.append(path.pop())
                print(visit)
            DFS(graph, path, visit)
        return visit[::-1]
    return DFS(graph, ["ICN"], [])
        
        
        
    answer = 0
    return answer