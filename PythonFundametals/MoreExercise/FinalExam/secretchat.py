text = input()

command = input()

def space_insert (text, index):
    text = text[:index] + ' ' + text[index::]
    print (text)
    return text

def reverse (text, string):
    if string in text:
        reverse_string = string[::-1]
        text = text.replace(string, '', 1)
        text = text + reverse_string
        print (text)
    else:
        print ('error')

    return text


while command != 'Reveal':
    command = command.split(':|:')

    if command[0] == 'InsertSpace':
        index = int(command[1])
        text = space_insert(text, index)

    elif command[0] == 'Reverse':
        string_to_reverse = command[1]
        text = reverse(text, string_to_reverse)
        
    else:
        substring = command[1]
        replacement = command[2]
        text = text.replace(substring, replacement)
        print (text)
    command = input()

print (f'You have a new text message: {text}')