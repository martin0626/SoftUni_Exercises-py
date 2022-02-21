words = input().split()

command = input()
while command != 'Stop':
    command = command.split()

    if command[0] == 'Delete' and 0 <= int(command[1]) < len(words) - 1:
        words.pop(int(command[1]) + 1)

    elif command[0] == 'Swap' and command[1] in words and command[2] in words:
        index_1 = words.index(command[1])
        index_2 = words.index(command[2])
        words[index_1], words[index_2] = words[index_2], words[index_1]

    elif command[0] == 'Put' and 0 <= int(command[2]) < len(words):
        if int(command[2]) == len(words) -1:
            words.append(command[1])
        else:
            words.insert(int(command[2]) - 1, command[1])

    elif command[0] == 'Sort':
        words = sorted(words)
        words.reverse()
    elif command[0] == 'Replace' and command[2] in words:
        index = words.index(command[2])
        words[index] = command[1]
    command = input()
        
print (' '.join(words))