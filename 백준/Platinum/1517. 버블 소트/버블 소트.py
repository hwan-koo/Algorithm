# 병합 정렬 구현
import sys

input = sys.stdin.readline
answer = 0

# 병합 정렬 함수
def merge_sort(s, e):
    global answer
    # 시작점과 끝점이 같으면 그대로 리턴
    if e - s < 1:
        return
    median = int(s + (e - s) / 2)
    merge_sort(s, median)
    merge_sort(median + 1, e)
    for i in range(s, e + 1):
        temp[i] = A[i]
    k = s
    index1 = s
    index2 = median + 1
    # 그룹 병합 로직
    while index1 <= median and index2 <= e:
        if temp[index1] > temp[index2]:
            A[k] = temp[index2]
            #뒷 그룹의 값이 더 작을 때 이동한 횟수를 결괏값에 저장
            answer += index2 - k
            k += 1
            index2 += 1
        else:
            A[k] = temp[index1]
            k += 1
            index1 += 1
        # 한 쪽 그룹이 모두 선택 되었을 때 남은 그룹 정리
    while index1 <= median:
        A[k] = temp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = temp[index2]
        k += 1
        index2 += 1


N = int(input())
A = list(map(int, input().split()))
temp = [0] * (N + 1)
A.insert(0, 0) # 병합 정렬을 위해서 0번 Index에 dummy value 삽

merge_sort(1, N)
print(answer)