import random

with open("words.txt") as words_list:
    lines = words_list.readlines()
    random_word = random.choice(lines)
    
print(random_word)