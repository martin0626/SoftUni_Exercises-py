text = input()


while text != 'end':
    new_text = ''
    for index in range (len(text) - 1, -1, -1):
        new_text += text[index]
    print(text, '=', new_text)
    text = input()




