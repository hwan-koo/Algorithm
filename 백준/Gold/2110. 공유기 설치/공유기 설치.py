import sys
input = sys.stdin.readline
N, C = map(int, input().split())
home_list = [int(input()) for _ in range(N)]
home_list.sort()
#집의 최소 최대 거리
start = 1
end = home_list[-1] - home_list[0]


while start <= end:
    mid = (start + end) // 2
    count = 1
    current = home_list[0]
    for i in range(N):
        if home_list[i] - current >= mid:
            count += 1
            current = home_list[i]
    if count >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
