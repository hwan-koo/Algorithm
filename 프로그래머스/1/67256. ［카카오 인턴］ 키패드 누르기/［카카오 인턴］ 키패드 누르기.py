def solution(numbers, hand):
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    left = "*"
    right = "#"
    answer = ""
    for i in numbers:
        if i in [1,4,7]:
            left = i 
            answer += "L"
        elif i in [3, 6, 9]:
            right = i
            answer += "R"
        else:
            left_i_j = [-1,-1]
            right_i_j = [-1,-1]
            target_i_j = [-1,-1]
            for a in range(4):
                for b in range(3):
                    if phone[a][b] == left:
                        left_i_j =[a,b]
                    if phone[a][b] == right:
                        right_i_j = [a,b]
                    if phone[a][b] == i:
                        target_i_j = [a,b]
            
            diff_l = abs(target_i_j[0] - left_i_j[0]) + abs(target_i_j[1] - left_i_j[1])
            diff_r = abs(target_i_j[0] - right_i_j[0]) + abs(target_i_j[1] - right_i_j[1])
            print(diff_l, diff_r)
            if diff_l < diff_r:
                left = i
                answer += "L"
            elif diff_l > diff_r:
                right = i
                answer += "R"
            else:
                if hand == "right":
                    right = i
                    answer += "R"
                else:
                    left = i
                    answer += "L"
    return answer