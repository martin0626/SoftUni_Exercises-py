import re

n = int(input())
pattern = r'\|(?P<name>[A-Z]{4,})\|:#(?P<title>[A-Za-z]+\s[A-Za-z]+)#'


for _ in range (n):
    text = input()
    matches = re.match(pattern, text)
    if matches:
        valid = matches.groupdict()
        name = valid['name']
        title = valid['title']
        strenght = len(name)
        armour = len(title)
        print (f'{name}, The {title}')
        print (f'>> Strength: {strenght}\n>> Armour: {armour}')
    else:
        print ('Access denied!')
        

