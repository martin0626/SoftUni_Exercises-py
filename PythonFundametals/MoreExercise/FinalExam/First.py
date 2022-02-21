text = input()


command_data = input()

while command_data != 'Done':
    command_data = command_data.split()
    command = command_data[0]

    if command == 'Change':
        text = text.replace(command_data[1], command_data[2])
        print (text)
        
    elif command == 'Includes':
        string_to_check = command_data[1]
        if string_to_check in text:
            print ('True')
        else:
            print ('False')
    elif command == 'End':
        list_text = text.split()
        if command_data[1] == list_text[-1]:
            print ('True')
        else:
            print ('False')
    
    elif command == 'Uppercase':
        text = text.upper()
        print (text)
        
    elif command == 'FindIndex':
        char = command_data[1]
        index = 0
        for x in range (len(text)):
            if text[x] == char:
                index = x
                break
        print (index)

    elif command == 'Cut':
        start_index = int(command_data[1])
        lenght = int(command_data[2])
        text = text[start_index: start_index + lenght]
        print (text)
        
    command_data = input()