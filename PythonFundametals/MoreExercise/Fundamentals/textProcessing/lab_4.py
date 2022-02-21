words_ban = input().split(', ')

text = input()


for word in words_ban:
    if word in text:
        text = text.replace(word, len(word) * '*')

print (text)

