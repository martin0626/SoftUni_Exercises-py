import re
text = ''
string = input()
while string != '':
    text += ' ' + string
    string = input()


pattern = re.findall(r'[0-9]+', text)

print (*pattern)
