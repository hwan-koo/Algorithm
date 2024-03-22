def solution(numbers, target):
    answer = []
    def DFS(nums, start, operator, value):
        if operator == "+":
            temp = nums[start] + value
        else:
            temp = value - nums[start]
        if start == len(nums) - 1:
            if temp == target:
                answer.append(1)
        else:
            DFS(nums, start + 1, "-", temp)
            DFS(nums, start + 1, "+", temp)
    DFS(numbers, 0, "+", 0)
    DFS(numbers, 0, "-", 0)
    
    return len(answer)