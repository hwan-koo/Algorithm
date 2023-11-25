def solution(arr):
    row = len(arr)
    column = len(arr[0])
    if row > column:
        for i in arr:
            for _ in range(row - column):
                i.append(0)
    elif column > row:
         for _ in range(column - row):
                arr.append([0] * column)
    answer = arr
    return answer