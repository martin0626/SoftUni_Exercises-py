from collections import OrderedDict 
from operator import getitem

n = int(input())
heroes_stats = {}
for _ in range (n):
    hero, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heroes_stats[hero] = {'HP': hp, 'MP': mp}
# print (heroes_stats['Solmyr']['hp'])

command = input()

while command != 'End':
    command = command.split(' - ')

    if command[0] == 'TakeDamage':
        hero_damaged = command[1]
        attacker = command[3]
        damage_taken = int(command[2])
        heroes_stats[hero_damaged]['HP'] -= damage_taken
        if heroes_stats[hero_damaged]['HP'] > 0:
            print (f'{hero_damaged} was hit for {damage_taken} HP by {attacker} and now has {(heroes_stats[hero_damaged]["HP"])} HP left!')
            
        else:
            print (f'{hero_damaged} has been killed by {attacker}!')
            del heroes_stats[hero_damaged]
            


    elif command[0] == 'Heal':
        hero_name = command[1]
        heal = int(command[2])
        
        if (heroes_stats[hero_name]['HP'] + heal) > 100:
            heal = 100 - heroes_stats[hero_name]['HP']
            print (f"{hero_name} healed for {heal} HP!")
            heroes_stats[hero_name]['HP'] = 100
        else:
            heroes_stats[hero_name]['HP'] += heal
            print (f"{hero_name} healed for {heal} HP!")


            

    elif command[0] == 'Recharge':
        hero_name = command[1]
        mana = int(command[2])
        if (heroes_stats[hero_name]['MP'] + mana) > 200:
            mana = 200 - heroes_stats[hero_name]['MP']
            print (f"{hero_name} recharged for {mana} MP!")
            heroes_stats[hero_name]['MP'] = 200
        else:
            heroes_stats[hero_name]['MP'] += mana
            print (f"{hero_name} recharged for {mana} MP!")



    elif command[0] == 'CastSpell':
        hero_name = command[1]
        mana_needed = int(command[2])
        spell = command[3]
        if heroes_stats[hero_name]['MP'] >= mana_needed:
            heroes_stats[hero_name]['MP'] -= mana_needed
            print (f"{hero_name} has successfully cast {spell} and now has {heroes_stats[hero_name]['MP']} MP!")
        else:
            print (f"{hero_name} does not have enough MP to cast {spell}!")

    command = input()

heroes_stats = dict(OrderedDict(sorted(heroes_stats.items(), key = lambda x: (-getitem(x[1], 'HP'), x[0]))))
for name, stats in heroes_stats.items():
    print (name)
    for key, value in stats.items():
        print (f'  {key}: {value}')

