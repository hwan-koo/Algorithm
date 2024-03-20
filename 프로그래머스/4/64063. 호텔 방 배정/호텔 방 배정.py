import sys
sys.setrecursionlimit(10000)
def findRoom(check, rooms):
    if check not in rooms:
        rooms[check] = check + 1 # 다음 빈 방을 알려줌, ex) 3번방 왔어? 아 이제 여기 꽉차서 다음 빈방은 4번방일거야
        return check
    empty = findRoom(rooms[check],rooms)
    rooms[check] = empty + 1 # 다음 빈 방을 알려줌
    return empty

def solution(k, room_number):
    rooms = dict()
    for i in room_number:
        findRoom(i, rooms)

    answer = list(rooms)
    return answer