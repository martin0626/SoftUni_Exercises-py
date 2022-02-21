start_points = int(input())
counter = 0
while start_points > 0:
    counter += 1
    sector = input()
    if sector == 'bullseye':
        print (f'Congratulations! You won the game with a bullseye in {counter} moves!')
        break
    
    points = int(input())
    
    if sector == 'number section':
        start_points -= points
    elif sector == 'double ring':
        start_points -= 2 * points
    elif sector == 'triple ring':
        start_points -= 3 * points
   

if start_points == 0:
    print (f'Congratulations! You won the game in {counter} moves!')

elif start_points < 0:
    print (f'Sorry, you lost. Score difference: {abs(start_points)}.')

