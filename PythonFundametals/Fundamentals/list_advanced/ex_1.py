words = input().split(', ')
words_to_check = input().split(', ')
lsit_of_matches = []

for word in words:
    for word_to_check in  words_to_check:
        if word in word_to_check and word not in lsit_of_matches:
            lsit_of_matches.append(word)
print (lsit_of_matches)
