spellbook = {}

command_data = input()


while command_data != 'End':
    command_data = command_data.split()

    command = command_data[0]

    if command == 'Enroll':
        hero_name = command_data[1] 
        if hero_name not in spellbook:
            spellbook[hero_name] = []
        else:
            print (f'{hero_name} is already enrolled.')
    elif command == 'Learn':
        spell = command_data[2]
        name_to_learn = command_data[1]
        if name_to_learn in spellbook and spell not in spellbook[name_to_learn]:
            spellbook[name_to_learn].append(spell)
        elif name_to_learn not in spellbook:
            print (f"{name_to_learn} doesn't exist.")
        elif spell in spellbook[name_to_learn]:
            print (f"{name_to_learn} has already learnt {spell}.")
    else:
        spell_to_remove = command_data[2]
        name_to_unlearn = command_data[1]
        if name_to_unlearn in spellbook and spell_to_remove in spellbook[name_to_unlearn]:
            spellbook[name_to_unlearn].remove(spell_to_remove)
        elif name_to_unlearn not in spellbook:
            print (f"{name_to_unlearn} doesn't exist.")
        elif spell_to_remove not in spellbook[name_to_unlearn]:
            print (f"{name_to_unlearn} doesn't know {spell_to_remove}.")            

    command_data = input()

spellbook = dict(sorted(spellbook.items(), key=lambda item: (-len(item[1]), item[0])))
print ('Heroes:')
for key in spellbook.keys():
    print (f'== {key}: {", ".join(spellbook[key])}')
