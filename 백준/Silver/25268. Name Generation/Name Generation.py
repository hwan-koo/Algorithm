import string
import random
N = int(input())
vowels = ["a", "e", "i", "o", "u"]
consonants = list(set(string.ascii_lowercase) - set(vowels))
answer_list = set()
index = 0
while len(answer_list) < N:
    answer = ""
    num = random.randrange(3, 21)
    for i in range(num):
        if i >= 2:
            if answer[i-2] in vowels and answer[i-1] in vowels:
                K = consonants
                randomLetter = str(random.choice(K))
                answer += randomLetter
            elif answer[i-2] in consonants and answer[i-1] in consonants:
                K = vowels
                randomLetter = str(random.choice(K))
                answer += randomLetter
            else:
                randomLetter = str(random.choice(string.ascii_lowercase))
                answer += randomLetter
        else:
            randomLetter = str(random.choice(string.ascii_lowercase))
            answer += randomLetter
    answer_list.add(answer)

for i in answer_list:
    print(i)
