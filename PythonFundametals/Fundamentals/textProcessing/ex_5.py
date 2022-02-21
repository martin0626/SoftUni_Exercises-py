text = input()

emojis = []
for x in text:
    index = text.index(x)
    if x == ':':
        
        emoji = x + text[index + 1]
        text = text.replace(text[index], '?', 1)
        if emoji not in emojis:
            emojis.append(emoji)

print ('\n'.join(emojis))



