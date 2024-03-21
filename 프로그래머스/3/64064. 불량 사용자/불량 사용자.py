import itertools
import re
def solution(user_id, banned_id):
    #밴 당할 모든 경우의 수
    a = itertools.permutations(user_id,len(banned_id))
    answer = []
    banned = " ".join(banned_id).replace("*",".")
    #banned_id의 조건 고려하기
    for i in a:
        if re.fullmatch(banned, " ".join(i)):
            answer.append(" ".join(sorted(i)))
    return len(set(answer))