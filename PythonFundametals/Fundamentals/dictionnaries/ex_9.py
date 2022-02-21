def add_user (forcces_dict, side_to_join, user_to_add):
    for side, users in forcces_dict.items():
        if user_to_add in users:
            return forcces_dict
    if side_to_join not in forcces_dict:
        forcces_dict[side_to_join] = []
        forcces_dict[side_to_join].append(user_to_add)
    else:
        if user_to_add not in forcces_dict[side_to_join]:
            forcces_dict[side_to_join].append(user_to_add)
    return forcces_dict

def transfer_user (forcces_dict, side_to_transfer, user_to_transfer):
    for side, users in forcces_dict.items():
        if user_to_transfer in users:
            forcces_dict[side].remove(user_to_transfer)
            return add_user(forcces_dict, side_to_transfer, user_to_transfer)
    return add_user(forcces_dict, side_to_transfer, user_to_transfer)

command = input()
sides_paricipants = {}

while command != 'Lumpawaroo':
    

    if '|' in command:
        command = command.split(' | ')
        side = command[0]
        participant = command[1]
        sides_paricipants = add_user(sides_paricipants, side, participant)
       

    else:
        command = command.split(' -> ')
        side = command[1]
        participant = command[0]
        sides_paricipants = transfer_user(sides_paricipants, side, participant)
        print (f'{participant} joins the {side} side!')
    command = input()
sides_paricipants = dict(sorted(sides_paricipants.items(), key=lambda item: (-len(item[1]),item[0])))

for key, value in sides_paricipants.items():
    if len(sides_paricipants[key]) > 0:
        print (f'Side: {key}, Members: {len(sides_paricipants[key])}')
        for man in sorted(value):
            print (f'! {man}')



        


