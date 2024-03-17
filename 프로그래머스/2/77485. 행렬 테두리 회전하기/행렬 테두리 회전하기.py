
def rotate(x1, y1, x2, y2,matrix):
        init = matrix[x1][y1]
        mini = init
        
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i+1][y1]
            mini = min(matrix[i+1][y1], mini)
        for i in range(y1, y2):
            matrix[x2][i] = matrix[x2][i+1]
            mini = min(matrix[x2][i+1], mini)
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i-1][y2]
            mini = min(matrix[i-1][y2], mini)
        for i in range(y2, y1, -1):
            matrix[x1][i] = matrix[x1][i-1]
            mini = min(matrix[x1][i-1], mini)
        matrix[x1][y1+1] = init
        return mini
def solution(rows, columns, queries):
    matrix = [ [(i) * columns + (j+1) for j in range(columns)] for i in range(rows)]
    
    answer = []
    for i in queries:
        a, b, c, d = i
        answer.append(rotate(a-1,b-1,c-1,d-1,matrix))
    
    return answer