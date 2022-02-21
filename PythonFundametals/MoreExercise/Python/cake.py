width = int(input())
lenght = int(input())
pieces = width * lenght
get_pieces = 0

while get_pieces != 'Stop':

    get_pieces = int(get_pieces)
    pieces -= get_pieces
    if pieces < 0:
        break
    get_pieces = input()

if pieces > 0:
    print (f'{pieces} pieces left.')

else:
    print (f'No more cake! You need {abs(pieces)} more pieces.')


