text = input()
result = ''
force = 0
index = 0

while index < len(text):
    if text[index] != '>':
        result += text[index]
        index += 1

    else:
        result += '>'
        index += 1
        force += int(text[index])
        while force > 0 and text[index] != '>':
            index += 1
            force -= 1
            if index >= len(text):
                break
print (result)
            

        