word = list(input())

index = 0
start = 0

while index < len(word):
    if word[index] == "<":
        index += 1
        while word[index] != ">":
            index += 1
        index += 1
    elif word[index].isalnum():
        start = index
        while index < len(word) and word[index].isalnum():
            index += 1
        temp = word[start:index]
        temp.reverse()
        word[start:index] = temp
    else:
        index += 1
print("".join(word))