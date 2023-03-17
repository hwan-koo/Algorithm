def solution(my_string):
    my_string = list(my_string)
    for i in my_string[:]:
        if i in ["a","e","i","o","u"]:
            my_string.remove(i)
    answer = "".join(my_string)
    return answer