def solution(word):
    data = []
    def diction(data, s, depth):
        if depth == 6:
            return
        if s != "":
            data.append(s)
        for i in ["A", "E", "I", "O", "U"]:
            diction(data, s + i, depth + 1)
    
    diction(data, "", 0)
            
    answer = data.index(word) + 1
    return answer