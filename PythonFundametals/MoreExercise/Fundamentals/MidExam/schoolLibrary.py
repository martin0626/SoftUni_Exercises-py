books_shelf = input().split('&')

command = input()

while command != 'Done':
    command = command.split(' | ')
    if command[0] == 'Add Book' and command[1] not in books_shelf:
        books_shelf.insert(0, command[1])
    elif command[0] == 'Take Book' and command[1] in books_shelf:
        books_shelf.remove(command[1])
    elif command[0] == 'Swap Books' and command[1] in books_shelf and command[2] in books_shelf:
        index_1 = books_shelf.index(command[1])
        index_2 = books_shelf.index(command[2])
        books_shelf[index_1], books_shelf[index_2] = books_shelf[index_2], books_shelf[index_1]

    elif command[0] == 'Insert Book':
        books_shelf.append(command[1])

    elif command[0] == 'Check Book' and 0 <= int(command[1]) < len(books_shelf):
        print (books_shelf[int(command[1])])

    command = input()

print (', '.join(books_shelf))



