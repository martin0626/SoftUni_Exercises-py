import re

n = int(input())
pattern = r'.*([\*@])(?P<word>[A-Z][a-z]{2,})\1:\s\[(?P<char_1>[A-Za-z])\]\|\[(?P<char_2>[A-Za-z])\]\|\[(?P<char_3>[A-Za-z])\]\|(?!.+)'

for _ in range (n):
    text = input()
    matches = re.match(pattern, text)
    if matches:     
        valid = matches.groupdict()
        first = ord(valid['char_1'])
        second = ord(valid['char_2'])
        third = ord(valid['char_3'])
        word = valid['word']
        print (f'{word}: {first} {second} {third}')
    else:
        print ('Valid message not found!')
