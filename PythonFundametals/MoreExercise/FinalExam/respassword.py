new_pass = input()

command = input()
def take_odd (text):
    result = ""
    for index in range (0, len(text)):
        if index % 2 != 0:
            result += text[index]
    return result

def cut (str_new, start, lenght):
    
    str_new = str_new[:start] + str_new[start + lenght:]
    return str_new

def subs (string_sub, new, old):
    
    if old in string_sub:
        string_sub = string_sub.replace(old, new)
        return string_sub
    else:
        print ('Nothing to replace!')

while command != 'Done':
    command = command.split()
    
    if command[0] == 'TakeOdd':
        new_pass = take_odd(new_pass)
        print (new_pass)
        
    elif command[0] == 'Cut':
        start_index = int(command[1])
        lenght = int(command[2])
        new_pass = cut (new_pass, start_index, lenght)
        print (new_pass)
 
    elif command[0] == 'Substitute':
        if command[1] in new_pass:
            old_string = command[1]
            new_string = command[2]
            new_pass = subs(new_pass, new_string, old_string)
            print (new_pass)

        else:
            old_string = command[1]
            new_string = command[2]
            subs(new_pass, new_string, old_string)

    command = input()
 
print (f'Your password is: {new_pass}')