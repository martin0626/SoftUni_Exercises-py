from math import floor

player_name = input()
games_played = int(input())
counter_volleyball = 0
counter_tennis = 0
counter_badminton = 0 
points_v = 0
points_t = 0
points_b = 0
for x in range (games_played):
    game = input()
    points = int(input())

    if game == 'volleyball':
        counter_volleyball += 1
        points_v += points + (0.07 * points)


    elif game == 'tennis':
        counter_tennis += 1
        points_t += points + (0.05 * points)
    

    elif game == 'badminton':
        counter_badminton += 1
        points_b += points + (0.02 * points)

sum_v = floor(points_v / counter_volleyball)
sum_t = floor(points_t / counter_tennis)
sum_b = floor(points_b / counter_badminton)
total = points_b + points_t + points_v
if sum_v >= 75 and sum_t >= 75 and sum_b >= 75:
    
    print (f'Congratulations, {player_name}! You won the cruise games with {floor(total)} points.')

else:
    print (f'Sorry, {player_name}, you lost. Your points are only {floor(total)}.')