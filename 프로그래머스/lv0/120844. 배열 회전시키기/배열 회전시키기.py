def solution(numbers, direction):
    if direction == "right":
        numbers.reverse()
        numbers.append(numbers.pop(0))
        numbers.reverse()
        return numbers
    else:
        numbers.append(numbers.pop(0))
        return numbers