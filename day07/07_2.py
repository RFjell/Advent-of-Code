import re

def check_ssl(supernet, hypernet):
    for i in range(len(supernet)):
        if is_aba_and_bab_exists(supernet[i], hypernet):
            return True
    return False

def is_aba_and_bab_exists(word, hypernet):
    for i in range(len(word)-2):
        # is aba?
        if word[i] == word[i+2] and word[i+1] != word[i] and word[i] != word[i+1]:
            bab = word[i+1] + word[i] + word[i+1]
            # check for bab
            for x in hypernet:
                if bab in x:
                    return True
    return False

with open('input') as f:
    lines = f.readlines()

count = 0

for line in lines:
    word_list = re.split('\[|\]', line)
    supernet = [ x for x in word_list[0::2]]
    hypernet = [ x for x in word_list[1::2]]

    if check_ssl(supernet, hypernet):
        count += 1
print(count)
