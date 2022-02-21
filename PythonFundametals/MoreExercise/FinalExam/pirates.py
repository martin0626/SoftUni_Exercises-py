from collections import OrderedDict 
from operator import getitem

command = input()
cities = {}
def plunder_event (town, people, gold, all_cities):
    all_cities[town]['population'] -= people
    all_cities[town]['gold'] -= gold
    print (f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
    if all_cities[town]['population'] == 0 or all_cities[town]['gold'] == 0:
        print (f'{town} has been wiped off the map!')
        del all_cities[town]
    return all_cities


def prosper_event(town, gold, all_cities):
    if gold < 0:
        print (f'Gold added cannot be a negative number!')
        
    else:
        all_cities[town]['gold'] += gold
        print (f'{gold} gold added to the city treasury. {town} now has {all_cities[town]["gold"]} gold.')
    return all_cities


while command != 'Sail':
    city, population, gold = command.split('||')
    population = int(population)
    gold = int(gold)

    if city not in cities:
        cities[city] = {'population' : population, 'gold': gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    command = input()

event = input()

while event != 'End':
    event = event.split('=>')

    if event[0] == 'Plunder':
        town = event[1]
        people_to_kill = int(event[2])
        gold_to_steal = int(event[3])
        cities = plunder_event (town, people_to_kill, gold_to_steal, cities)
       
 
    else:
        town = event[1]
        gold = int(event[2])
        cities = prosper_event(town, gold, cities)
    event = input()


cities = dict(OrderedDict(sorted(cities.items(), key = lambda x: (-getitem(x[1], 'gold'), x[0]))))



print (f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
for town in cities.keys():
    people = cities[town]['population']
    gold = cities[town]['gold']
    print (f'{town} -> Population: {people} citizens, Gold: {gold} kg')
    




    