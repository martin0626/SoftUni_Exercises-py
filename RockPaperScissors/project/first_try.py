from random import randint

choices = ['Rock', 'Paper', 'Scissor']


def winner(auto, man):
    if auto == 'Rock' and man == 'Paper':
        return 'You win, versus Rock!!!'

    elif auto == 'Paper' and man == 'Scissor':
        return 'You win, versus Paper!!!'

    elif auto == 'Scissor' and man == 'Rock':
        return 'You win versus scissors!!!'

    elif auto == man:
        return 'Draw!'

    else:
        return 'You are loser!!!'


while True:
    player_choice = input('Make your choice: ')

    if player_choice == 'End':
        break

    if player_choice not in choices:
        print('Please make your choice from the given one: Rock, Paper, Scissor')
        continue

    auto_choice = choices[randint(0, len(choices) - 1)]
    print(winner(auto_choice, player_choice))


