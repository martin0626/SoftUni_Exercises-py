import re

text = input()

pattern_1 = r'(\*\*|::)[A-Z][a-z][a-z]+\1'

matches = re.finditer(pattern_1, text)
valid_emojis = [x.group() for x in matches]

cool_emojis = {}
def coolness_sum (coolness):
    result = 1
    for x in coolness:
        result *= int(x)
    return result

for emoji in valid_emojis:
    coolness_emojies = 0
    for digit in emoji[1:len(emoji) -2]:
        coolness_emojies += ord(digit)
    if emoji not in cool_emojis:
        cool_emojis[emoji] = coolness_emojies

coolness = re.findall('\\d', text)

sum_coolness = coolness_sum(coolness)
print (f'Cool threshold: {sum_coolness}')
print (f'{len(cool_emojis)} emojis found in the text. The cool ones are:')
for emj in cool_emojis.keys():
    if cool_emojis[emj] >= sum_coolness:
        print (emj)
