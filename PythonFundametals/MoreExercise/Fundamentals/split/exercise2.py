parts = input().split('|')
command = input().split()
while command[0] !='Done':
    if len(command)>2:
        index = int(command[2])
    if command[0] == 'Move' and command[1] == 'Left':
        if index <= len(parts) and index > 0:
            parts[index - 1], parts[index] = parts[index], parts[index - 1]
            


    elif command[0] == 'Move' and command[1] == 'Right':
        if index < len(parts):
            parts[index], parts[index + 1] = parts[index+ 1], parts[index]
            


    elif command[0] == 'Check' and command[1] == 'Even':
        for index, num in enumerate(parts):
            if index % 2 == 0:
                print (num)
    else:
        for index, num in enumerate(parts):
            
            if index % 2 != 0:
                print (num)
            
    
            
    command = input().split()
name = ''
for x in parts:
    name += x
print (f'You crafted {name}!')
