n = int(input())

pieces = {}


for _ in range (n):
    data = input().split('|')
    piece = data[0]
    composer = data[1]
    key = data[2]
    pieces[piece] = {'composer': composer, 'key':key}
   

commands_date = input()

while commands_date != 'Stop':
    commands_date = commands_date.split('|')

    command = commands_date[0]

    if command == 'Add':
        piece_to_add = commands_date[1]
        composer_to_add = commands_date[2]
        key_to_add = commands_date[3]
        if piece_to_add not in pieces:
            pieces[piece_to_add] = {'composer': composer_to_add, 'key': key_to_add}
            print (f"{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!")

        else:
            print (f"{piece_to_add} is already in the collection!")

    elif command == 'Remove':
        piece_to_remove = commands_date[1]
        if piece_to_remove in pieces:
            del pieces[piece_to_remove]
            print (f"Successfully removed {piece_to_remove}!")
        else:
            print (f"Invalid operation! {piece_to_remove} does not exist in the collection.")
    else:
        piece_to_change = commands_date[1]
        new_key = commands_date[2]
        if piece_to_change in pieces:
            pieces[piece_to_change]['key'] = new_key
            print (f"Changed the key of {piece_to_change} to {new_key}!")
        else:
            print (f"Invalid operation! {piece_to_change} does not exist in the collection.")
    commands_date = input()

pieces = dict(sorted(pieces.items(), key = lambda x: (x[0], x[1]['composer'])))
for key in pieces.keys():
    print (f"{key} -> Composer: {pieces[key]['composer']}, Key: {pieces[key]['key']}")