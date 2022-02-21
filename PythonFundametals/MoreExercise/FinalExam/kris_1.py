skill = input()

command_data = input()

while command_data != 'For Azeroth':
    command_data = command_data.split(' ')
    command = command_data[0]

    if command == 'GladiatorStance':
        skill = skill.upper()
        print (skill)
    elif command == 'DefensiveStance':
        skill = skill.lower()
        print (skill)

    elif command == 'Dispel':
        index_replace = int(command_data[1])
        letter = command_data[2]
        if 0 <= index_replace < len(skill):
            skill = skill[:index_replace] + letter + skill[index_replace + 1::]
            print ('Success!')
        else:
            print ('Dispel too weak.')
    elif command == 'Target' and command_data[1] == 'Change':
        substring_to_change = command_data[2]
        second_substring = command_data[3]
        skill = skill.replace(substring_to_change, second_substring)
        print (skill)
    elif command == 'Target' and command_data[1] == 'Remove':
        substring_to_remove = command_data[2]
        skill = skill.replace(substring_to_remove, '')
        print (skill)
    else:
        print ("Command doesn't exist!")
    command_data = input()



