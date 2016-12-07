import re

def check_abba(word_list):
    res = False
    for i in range(len(word_list)):
        if i % 2 == 0:
            if is_abba(word_list[i]):
                res = True
        else:
            if is_abba(word_list[i]):
                return False
    return res

def is_abba(word):
    for i in range(len(word)-3):
        if word[i] == word[i+3] and word[i+1] == word[i+2] and word[i] != word[i+1]:
            return True
    return False

with open('input') as f:
    lines = f.readlines()

count = 0

for line in lines:
    word_list = re.split('\[|\]', line)

    if check_abba(word_list):
        count += 1
print(count)
