def solution(n):
    nums = []
    num = n
    
    while num:
        num, digit = divmod(num,3)
        nums.append(str(digit))
    three = "".join(reversed(nums))
    
    answer = int(three[::-1],3)
    return answer