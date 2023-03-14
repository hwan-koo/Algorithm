def solution(numbers, k):
    numbers = numbers * 1000
    answer = numbers[2 * k - 2]
    return answer