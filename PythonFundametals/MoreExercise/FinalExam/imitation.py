def move(text, num_letters):
    first_part = text[:num_letters]
    text = text[num_letters:] + first_part
    return text
def insert_value(text, value, index):
    text = text[:index] + value + text[index:]
    return text

text = input()

command_data = input()


while command_data != 'Decode':
    command_data = command_data.split('|')

    command = command_data[0]

    if command == 'Move':
        num_letters = int(command_data[1])
        text = move(text, num_letters)
        


    elif command == 'Insert':
        index = int(command_data[1])
        value = command_data[2]
        text = insert_value(text, value, index)
        
        
    else:
        substring = command_data[1]
        replacement = command_data[2]
        text = text.replace(substring, replacement)
    command_data = input()

print (f'The decrypted message is: {text}')


