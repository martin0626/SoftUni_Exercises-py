text = input().split()

command = input()

while command != 'end':
    command = command.split()

    if command[0] == 'reverse':
        index_start = int(command[2])
        index_count = int(command[4])
        if index_start != 0:
            text = text[0:index_start] + text[index_start + index_count - 1:index_start - 1:-1] + text[index_start + index_count: ]
        else:
            text =text[index_start + index_count - 1::-1] + text[index_start + index_count: ]

    elif command[0] == 'sort':
        index_start = int(command[2])
        index_count = int(command[4])
        text = text[0:index_start] + sorted(text[index_start: index_start + index_count]) + text[index_start + index_count:]
        

    elif command[0] == 'remove':
        count = int(command[1])
        text = text[count:]
        
    
    command = input()

print (', '.join(text))