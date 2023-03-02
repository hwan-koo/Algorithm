def solution(numbers):
    def double(x):
        return 2 * x
    answer = list(map(double, numbers))
    return answer