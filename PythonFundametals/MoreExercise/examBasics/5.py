name = input()
most_goals = -1000000000000000
best_player = ''
hat_trick = False
while name != 'END':
    goals_num = int(input())

    if goals_num > most_goals:
        most_goals = goals_num
        best_player = name
        if goals_num >= 3:
            hat_trick = True
    if goals_num >= 10:
        break
    
    name = input()
        

print(f'{best_player} is the best player!')
if most_goals >= 10 or hat_trick:
    print (f'He has scored {most_goals} goals and made a hat-trick !!!')

else:
    print (f'He has scored {most_goals} goals.')


