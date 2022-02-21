import re 

text = input()


pattern = r'([#@])(?P<word_1>[A-Za-z][A-Za-z][A-Za-z]+)\1\1(?P<word_2>[A-Za-z][A-Za-z][A-Za-z]+)\1'

valid_words = re.finditer(pattern, text)

mirror_words = []

count = 0
for words in valid_words:
    count += 1
    words = words.groupdict()
    word_1_reversed = words['word_1'][::-1]
    if word_1_reversed == words['word_2']:
        result = f"{words['word_1']} <=> {words['word_2']}"
        mirror_words.append(result)

if count > 0:
    print (f'{count} word pairs found!')
else: 
    print ('No word pairs found!')

if len(mirror_words) > 0:
    print (f'The mirror words are: \n{", ".join(mirror_words)}')

else:
    print ('No mirror words!')


