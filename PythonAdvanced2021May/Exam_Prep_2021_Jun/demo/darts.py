import re


player_one, player_two = input().split(', ')
dartBoard = [input().split() for _ in range(7)]

player_one_points = 501
player_two_points = 501

winner = ''
player_one_moves = 0
player_two_moves = 0
current_go = 1


def calculate_points(current_row, current_col):
    cells_mapper = {'D': 2, 'T': 3, 'B': 501}
    left_num = int(dartBoard[current_row][0])
    right_num = int(dartBoard[current_row][len(dartBoard[0]) - 1])
    down_num = int(dartBoard[len(dartBoard) - 1][current_col])
    up_num = int(dartBoard[0][current_col])

    if dartBoard[current_row][current_col] in cells_mapper.keys():
        points_earned = (left_num + right_num + down_num + up_num) * cells_mapper[dartBoard[current_row][current_col]]
        print(points_earned)
        return points_earned
    else:
        return int(dartBoard[current_row][current_col])


while winner == '':
    input_data = input()
    row, col = [int(num) for num in re.findall(r'\d+', input_data)]

    if 0 <= row < 7 and 0 <= col < 7:
        points = calculate_points(row, col)

        if current_go % 2 != 0:
            player_one_points -= points
            player_one_moves += 1
            if player_one_points <= 0:
                print(f'{player_one} won the game with {player_one_moves} throws!')
                winner = player_one

        else:
            player_two_points -= points
            player_two_moves += 1
            if player_two_points <= 0:
                print(f'{player_two} won the game with {player_two_moves} throws!')
                winner = player_two

    current_go += 1
