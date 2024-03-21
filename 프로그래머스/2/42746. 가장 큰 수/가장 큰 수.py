def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = "".join(list(map(str,numbers)))
    if ["0"] * len(numbers) == numbers:
        return "0"
    return answer