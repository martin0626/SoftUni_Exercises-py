width = int(input())
lenght = int(input())
pieces = width * lenght
pieces_eaten = 0 
while pieces_eaten < pieces:
    pieces_need = input()
    if pieces_need == "STOP":
        break
    pieces_need = int(pieces_need)
    pieces_eaten += pieces_need

if pieces_eaten <= pieces:
    rest = pieces - pieces_eaten 
    print (f'{rest} pieces are left.')
else:
    needed = pieces_eaten - pieces
    print (f'No more cake left! You need {needed} pieces more.') 




