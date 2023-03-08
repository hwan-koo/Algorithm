def solution(num_list):
    h = 0
    j = 0
    for i in num_list:
        if i % 2 == 0:
            h += 1
        else:
            j += 1
    answer = [h,j]
    return answer