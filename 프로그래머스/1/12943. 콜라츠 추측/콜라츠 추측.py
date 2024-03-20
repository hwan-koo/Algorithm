
def collatz(count, number):
    if number == 1:
        return count
    if count == 500:
        return -1
    if number % 2 == 0:
        return collatz(count + 1, number // 2)
    else:
        return collatz(count + 1, number * 3 + 1)
def solution(num):
    return collatz(0, num)