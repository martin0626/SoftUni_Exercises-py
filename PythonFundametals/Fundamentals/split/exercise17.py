cards = input().split()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
less = False


for x in cards:
    x = x.split('-')
    team = x[0]
    player = int(x[1])
    if team == 'A':
        if player in A:
            A.remove(player)
    
    else:
        if player in B:
            B.remove(player)
    if len(A) < 7:
        less = True
        break
    if len(B) < 7:
        less = True
        break
print (f'Team A - {len(A)}; Team B - {len(B)}')
if less:
    print ('Game was terminated')
