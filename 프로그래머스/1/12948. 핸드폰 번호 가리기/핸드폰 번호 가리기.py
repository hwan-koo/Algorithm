import re
def solution(phone_number):
    answer = re.sub('\d(?=\d{4})','*',phone_number)
    
    return answer