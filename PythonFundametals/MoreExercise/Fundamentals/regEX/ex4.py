import re
text = input()


pattern = r'(^|(?<=\s))([\*@])(?P<word>[A-Z][a-z]{2,})\1(.+)?\s\[(?P<char_1>[A-Za-z])\]\|\[(?P<char_2>[A-Za-z])\]\|\[(?P<char_3>[A-Za-z])\]\|'
result = re.finditer(pattern, text)

for x in result:
    email = x.group()
    if email[-1] == '.':
        email = email[0:len(email) - 1]
    print (email)


